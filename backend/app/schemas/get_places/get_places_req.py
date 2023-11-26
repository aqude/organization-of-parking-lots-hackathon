from typing import Optional
from pydantic import BaseModel
from decimal import Decimal
import uuid


class GetPlaceReq(BaseModel):
    City: str
    City_id: int
    parking_longitude: Decimal
    parking_latitude: Decimal


class PlacesOut(BaseModel):
    id: uuid.UUID
    number_of_places: int
    description: Optional[str] = None
    price: Decimal
    parking_longitude: Decimal
    parking_latitude: Decimal
    City_id: int