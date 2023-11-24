from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import Places
from app.schemas.get_places import GetPlaceReq


async def get_place(session: AsyncSession, data: GetPlaceReq):
    query = select(Places).where(and_(Places.City_id == data.City_id, Places.number_of_place == data.number_of_place,
                                      Places.parking_latitude== data.parking_latitude, Places.parking_longitude == data.parking_longitude))
    result = await session.scalars(query)
    return result
