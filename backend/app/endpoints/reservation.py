from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from starlette.status import HTTP_200_OK, HTTP_204_NO_CONTENT
from app.db.models import User
from app.db.connection.session import get_sync_session
from app.utils.user.business_logic import get_current_user
from app.utils.reservations import (
    create_reservation,
    delete_reservation,
    get_reservations,
)
from app.schemas.reservations import ReservationIn, ReservationDelete, ReservationOut

api_router = APIRouter(
    prefix="/reservations",
    tags=["Reservation"],
)


@api_router.post("/create", response_model=ReservationOut)
async def create_parking_reservation(
    data: ReservationIn,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_sync_session),
):
    result = await create_reservation(data, user, db)
    return ReservationOut(**result.__dict__)


@api_router.delete(
    status_code=HTTP_204_NO_CONTENT, path="/delete", response_class=Response
)
async def delete_parking_reservation(
    data: ReservationDelete,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_sync_session),
):
    result = await delete_reservation(data, user, db)
    return result


@api_router.get(
    "/list",
    response_model=list[ReservationOut],
    status_code=HTTP_200_OK,
)
async def list_parking_reservations(
    user: User = Depends(get_current_user), db: Session = Depends(get_sync_session)
):
    result = await get_reservations(user, db)
    return [ReservationOut(**item.__dict__) for item in result]