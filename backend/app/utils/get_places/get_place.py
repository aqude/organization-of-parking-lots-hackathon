from typing import Optional
from sqlalchemy import select, and_
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import Places
from app.schemas.get_places import GetPlaceReq


async def get_place(session: AsyncSession, data: GetPlaceReq):
    query = select(Places).where(
        and_(
            Places.City_id == data.City_id,
            Places.parking_latitude == data.parking_latitude,
            Places.parking_longitude == data.parking_longitude,
        )
    )
    result = await session.scalars(query)
    return result


def get_place_by_id(session: Session, id: int) -> Optional[Places]:
    return session.query(Places).filter(Places.number_of_place == id).first()