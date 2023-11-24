from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel


class UpdatePlaceReq(BaseModel):
    number_of_place: int
    time_occupied_from: datetime
    time_occupied_to: datetime
    City_id: int
    parking_longitude: Decimal
    parking_latitude: Decimal
