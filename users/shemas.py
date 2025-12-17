from datetime import datetime
from pydantic import BaseModel, EmailStr

"""Pydantic схема для пользователей """


class UserSchema(BaseModel):
    id: int
    email: str
    created_at: datetime

    model_config = {"from_attributes": True}


class UserRead(UserSchema):
    pass


class UserCreate(BaseModel):
    email: EmailStr
