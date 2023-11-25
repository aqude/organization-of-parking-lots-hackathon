from datetime import timedelta
import uuid

from fastapi import APIRouter, Body, Depends, HTTPException, Request, Response
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.config import get_settings
from app.db.connection import get_session
from app.db.models import User
from app.schemas.auth import (
    RegistrationForm,
    RegistrationSuccess,
    Token,
    PaymentMethodIn,
    PaymentMethodOut,
)
from app.schemas.auth import User as UserSchema
from app.utils.user import (
    authenticate_user,
    create_access_token,
    delete_user,
    get_current_user,
    register_user,
    get_payment_methods,
)
from app.utils.payment.payment import confirm_payment
from app.utils.payment import create_payment_method


api_router = APIRouter(
    prefix="/user",
    tags=["User"],
)


@api_router.post(
    "/authentication",
    status_code=status.HTTP_200_OK,
    response_model=Token,
)
async def authentication(
    _: Request,
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: AsyncSession = Depends(get_session),
):
    user = await authenticate_user(session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=get_settings().ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@api_router.post(
    "/registration",
    status_code=status.HTTP_201_CREATED,
    response_model=RegistrationSuccess,
    responses={
        status.HTTP_400_BAD_REQUEST: {
            "description": "Bad parameters for registration",
        },
    },
)
async def registration(
    _: Request,
    registration_form: RegistrationForm = Body(...),
    session: AsyncSession = Depends(get_session),
):
    is_success, message = await register_user(session, registration_form)
    if is_success:
        return {"message": message}
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=message,
    )


@api_router.get(
    "/me",
    status_code=status.HTTP_200_OK,
    response_model=UserSchema,
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "Could not validate credentials",
        },
    },
)
async def get_me(
    _: Request,
    current_user: User = Depends(get_current_user),
):
    return UserSchema.from_orm(current_user)


@api_router.delete(
    "/takeout",
    status_code=status.HTTP_204_NO_CONTENT,
    response_class=Response,
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "Could not validate credentials",
        },
    },
)
async def takeout(
    _: Request,
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session),
):
    await delete_user(session, current_user)


@api_router.post(
    "/payment/method/add",
    status_code=status.HTTP_200_OK,
    response_model=dict,
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "Could not validate credentials",
        },
    },
)
async def add_payment_method(
    _: Request,
    payment_method: PaymentMethodIn = Body(...),
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session),
):
    return {
        "payment_url": await create_payment_method(
            session, current_user, payment_method
        )
    }


@api_router.get("/payment/method/check/{id}", status_code=status.HTTP_200_OK)
async def check_payment_method(
    _: Request,
    id: uuid.UUID,
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session),
):
    return {"response": await confirm_payment(session, current_user, id)}


@api_router.get(
    "/payment/method/list",
    status_code=status.HTTP_200_OK,
    response_model=list[PaymentMethodOut],
)
async def get_payment_method(
    _: Request,
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session),
):
    result = list(await get_payment_methods(session, current_user))
    return [PaymentMethodOut(type=item.type, title=item.title) for item in result]