from datetime import datetime

from pydantic import BaseModel, EmailStr, constr


class User(BaseModel):
    username: constr(min_length=1)
    email: EmailStr
    dt_created: datetime
    dt_updated: datetime

    class Config:
        orm_mode = True
