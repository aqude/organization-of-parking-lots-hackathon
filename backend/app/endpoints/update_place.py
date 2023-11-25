import datetime

from fastapi import APIRouter, Depends, HTTPException, Request, Body
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.db.connection import get_session
from app.db.models.user import User
from app.utils.update_place import update_place
from app.schemas.update_place import UpdatePlaceReq
from app.utils.user.business_logic import get_current_user


api_router = APIRouter(
    prefix="",
    tags=["UpdatePlaces"],
)


@api_router.post(
    "/update_place",
    status_code=status.HTTP_200_OK,
)
async def getplace(
    _: Request,
    session: AsyncSession = Depends(get_session),
    current_user: User = Depends(get_current_user),
    data: UpdatePlaceReq = Body(
        ...,
        example={
            "City_id": 113,
            "number_of_place": 1,
            "parking_longitude": 35.423,
            "parking_latitude": 34.433,
            "status": False,
            "payment_method_title": "Bank card 4444",
        },
    ),
):
    result = await update_place(session, data, current_user)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="place is already taken or invalid data",
        )
    return {"status": "succesfull"}