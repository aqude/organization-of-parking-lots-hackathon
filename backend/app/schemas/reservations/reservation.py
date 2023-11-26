from datetime import datetime
import uuid
from pydantic import BaseModel


class ReservationIn(BaseModel):
    parking_id: uuid.UUID
    payment_method_id: uuid.UUID


class ReservationDelete(BaseModel):
    id: uuid.UUID


class ReservationOut(BaseModel):
    id: uuid.UUID
    parking_id: uuid.UUID
    user_id: uuid.UUID
    payment_method_id: uuid.UUID
    start_time: datetime
    end_time: datetime