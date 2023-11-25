from datetime import datetime

from pydantic import BaseModel, EmailStr, constr


class User(BaseModel):
    first_name: constr(min_length=1)
    second_name: constr(min_length=1)
    last_name: constr(min_length=1)
    email: EmailStr
    dt_created: datetime
    dt_updated: datetime

    class Config:
        orm_mode = True


class UserAuth(BaseModel):
    email: EmailStr
    password: constr(min_length=8)
