from pydantic import BaseModel, EmailStr
from typing import Optional
from app.models.user import RoleEnum


class UserBase(BaseModel):
    username: str
    email: EmailStr
    role: RoleEnum
    address: Optional[str] = None
    phone: Optional[str] = None
    contact_person: Optional[str] = None



class UserCreate(UserBase):
    password: str  # raw password from request


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    role: Optional[RoleEnum] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    contact_person: Optional[str] = None


class UserRead(UserBase):
    id: int

    class Config:
        from_attributes = True
