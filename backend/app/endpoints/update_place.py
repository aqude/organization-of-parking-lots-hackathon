import datetime

from fastapi import APIRouter, Depends, HTTPException, Request, Body
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.db.connection import get_session
from app.schemas.update_place import UpdatePlaceReq


api_router = APIRouter(
    prefix="",
    tags=["UpdatePlaces"],
)