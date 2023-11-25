from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel
from typing import Optional


class UpdatePlaceReq(BaseModel):
    number_of_place: int
    City_id: int
    parking_longitude: Decimal
    parking_latitude: Decimal
    status: bool
    payment_method_title: Optional[str]