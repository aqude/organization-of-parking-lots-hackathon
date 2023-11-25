from pydantic import BaseModel
from decimal import Decimal


class GetPlaceReq(BaseModel):
    City: str
    City_id: int
    number_of_place: int
    parking_longitude: Decimal
    parking_latitude: Decimal