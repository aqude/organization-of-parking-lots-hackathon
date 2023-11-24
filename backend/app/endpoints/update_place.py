import datetime

from fastapi import APIRouter, Depends, HTTPException, Request, Body
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.db.connection import get_session
from app.utils.update_place import update_place
from app.schemas.update_place import UpdatePlaceReq


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
    data: UpdatePlaceReq = Body(..., example={"City_id": 113, "number_of_place": 1, "parking_longitude": 35.423,
                                            "parking_latitude": 34.433, "time_occupied_from": datetime.datetime.now(),
                                            "time_occupied_to": datetime.datetime.now()})
):
    result = await update_place(session, data)
    if not result:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="place is already taken or invalid data")
    return {"status": "succesfull"}
