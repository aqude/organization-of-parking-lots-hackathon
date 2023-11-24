from sqlalchemy import update, and_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import Places
from app.schemas.update_place import UpdatePlaceReq


async def update_place(session: AsyncSession, data: UpdatePlaceReq) -> bool:
    query_check_place = select(Places).where(and_(Places.time_occupied_from == None,
                                                Places.time_occupied_to == None,
                                                Places.parking_longitude == data.parking_longitude,
                                                Places.parking_latitude == data.parking_latitude,
                                                Places.number_of_place == data.number_of_place)).with_for_update()
    if query_check_place is None:
        return False
    query_for_update = update(Places).where(and_(Places.City_id == data.City_id,
                                                 Places.number_of_place == data.number_of_place,
                                                 Places.parking_longitude == data.parking_longitude,
                                                 Places.parking_latitude == data.parking_latitude,
                                                 )
                                            ).values(
        dict({"time_occupied_from": data.time_occupied_from, "time_occupied_to": data.time_occupied_to})
    )

    await session.execute(query_for_update)
    await session.commit()
    return True
