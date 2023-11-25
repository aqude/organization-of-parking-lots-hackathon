from decimal import Decimal
from pydantic import BaseModel


class GetPlacesRadReq(BaseModel):
    City_id: int
    radius: int
    lon: Decimal
    lat: Decimal
