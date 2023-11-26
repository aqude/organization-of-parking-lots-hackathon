from pydantic import BaseModel
import uuid

class ReviewIn(BaseModel):
    parking_id: uuid.UUID
    text: str
    

class ReviewOut(BaseModel):
    parking_id: uuid.UUID
    user_id: uuid.UUID
    user_fullname: str
    text: str