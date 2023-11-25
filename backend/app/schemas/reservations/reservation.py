import uuid
from pydantic import BaseModel


class ReservationIn(BaseModel):
    parking_id: uuid.UUID
    payment_method_id: uuid.UUID


class ReservationDelete(BaseModel):
    id: uuid.UUID