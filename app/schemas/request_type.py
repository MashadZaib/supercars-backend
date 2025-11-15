from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class RequestTypeBase(BaseModel):
    name: Optional[str] = Field(None)
    type: Optional[str] = Field(None)
class RequestTypeCreate(RequestTypeBase):
    pass

class RequestTypeRead(RequestTypeBase):
    id: int

    class Config:
        orm_mode = True
