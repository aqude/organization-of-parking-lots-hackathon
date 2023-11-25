from fastapi import APIRouter, Depends, HTTPException, Request, Body
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.db.connection import get_session
from app.config import get_settings
from app.utils.get_places import get_places, get_place
from app.utils.get_places_in_radius import get_places_in_radius
from app.schemas.get_places import GetPlaceReq
from app.schemas.get_places_in_radius import GetPlacesRadReq

api_router = APIRouter(
    prefix="",
    tags=["GetPlaces"],
)


@api_router.get(
    "/get_places",
    status_code=status.HTTP_200_OK,
)
async def getplaces(_: Request, session: AsyncSession = Depends(get_session)):
    result = list(await get_places(session))
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="not found")
    return result


@api_router.post(
    "/get_place",
    status_code=status.HTTP_200_OK,
)
async def getplace(
    _: Request,
    session: AsyncSession = Depends(get_session),
    data: GetPlaceReq = Body(
        ...,
        example={
            "City": "Белгород",
            "City_id": 113,
            "number_of_place": 1,
            "parking_longitude": 35.423,
            "parking_latitude": 34.433,
        },
    ),
):
    result = list(await get_place(session, data))
    if not result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid data"
        )
    return result


@api_router.post(
    "/get_places_in_radius",
    status_code=status.HTTP_200_OK,
)
async def get_places_radius(
    _: Request,
    session: AsyncSession = Depends(get_session),
    data: GetPlacesRadReq = Body(
        ..., example={"City_id": 113, "radius": 500, "lon": 35.423, "lat": 34.433}
    ),
):
    result = list(await get_places_in_radius(session, data, get_settings()))
    if not result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid data"
        )
    return result