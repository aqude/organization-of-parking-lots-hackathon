from sqlalchemy import update, and_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import Places
from app.db.models.user import User
from app.schemas.update_place import UpdatePlaceReq
from app.utils.reservations import create_reservation, delete_reservation


async def update_place(session: AsyncSession, data: UpdatePlaceReq, user: User) -> bool:
    query_place = select(Places).where(
        and_(
            Places.parking_longitude == data.parking_longitude,
            Places.parking_latitude == data.parking_latitude,
            Places.number_of_place == data.number_of_place,
        )
    )
    place = await session.scalar(query_place)
    if not place:
        return False
    query_for_update = (
        update(Places)
        .where(
            and_(
                Places.City_id == data.City_id,
                Places.number_of_place == data.number_of_place,
                Places.parking_longitude == data.parking_longitude,
                Places.parking_latitude == data.parking_latitude,
            )
        )
        .values(dict({"status": data.status}))
    )
    if data.status is False and place.status is True:
        await create_reservation(session, data, user)
    elif data.status is True and place.status is False:
        session, payment, reservation = await delete_reservation(session, place, user)
        if payment.status == "succeeded" or payment.status == "pending":
            payment.is_confirmed = True
            await session.delete(reservation)
    await session.execute(query_for_update)
    await session.commit()
    return True
