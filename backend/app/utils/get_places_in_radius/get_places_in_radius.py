import math
from decimal import Decimal

from sqlalchemy import select, and_, between
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.get_places_in_radius import GetPlacesRadReq
from app.config import DefaultSettings
from app.db.models import Places


async def computeDelta(coor: Decimal, eart_radius: Decimal) -> Decimal:
    return Decimal(math.pi) / 180 * eart_radius * Decimal(math.cos(await deg2rad(coor)))


async def deg2rad(coor: Decimal) -> Decimal:
    return coor * Decimal(math.pi) / 180


async def get_places_in_radius(session: AsyncSession, data: GetPlacesRadReq, settings: DefaultSettings):
    deltalat = await computeDelta(data.lat, settings.EART_RADIUS)
    deltalon = await computeDelta(data.lon, settings.EART_RADIUS)

    aroundlat = data.radius / (deltalat * 10)
    aroundlon = data.radius / (deltalon * 10)

    query = select(Places).where(Places.City_id == data.City_id).filter(
        and_(
            Places.parking_longitude.between(data.lon - aroundlon, data.lon + aroundlon),
            Places.parking_latitude.between(data.lat - aroundlat, data.lat + aroundlat)
        )
    )
    result = await session.scalars(query)
    if not result:
        return None
    return result
