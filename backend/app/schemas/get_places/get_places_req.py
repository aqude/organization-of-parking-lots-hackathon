import datetime

from pydantic import BaseModel
from decimal import Decimal


class GetPlacesResp(BaseModel):
    City: str
    City_id: int
    parking_longitude: Decimal
    parking_latitude: Decimal
    time_occupied_from: datetime.datetime
    time_occupied_to: datetime.datetime
    price_for_hour: int
    type_of_parking: str
