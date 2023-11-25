from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import Places


async def get_places(session: AsyncSession):
    query = select(Places)
    result = await session.scalars(query)
    return result
