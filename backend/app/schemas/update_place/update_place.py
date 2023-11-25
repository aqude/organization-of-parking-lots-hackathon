from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel
import uuid


class UpdatePlaceReq(BaseModel):
    id: uuid.UUID
    City_id: int
    parking_longitude: Decimal
    parking_latitude: Decimal
    number_of_places: int