from typing import Optional

from pydantic import BaseModel, EmailStr


class User(BaseModel):
    email: EmailStr
    telephone: str


class UserIn(User):
    password: str
    first_name: Optional[str] = "NR"
    last_name: Optional[str] = "NR"
    address: Optional[str] = "NR"


class UserOut(BaseModel):
    id: int
    first_name: str
    last_name: str
    address: str
    email: EmailStr
    telephone: str

    class Config:
        orm_mode = True
