from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class CargoTypeBase(BaseModel):
    name: Optional[str] = Field(None)
class CargoTypeCreate(CargoTypeBase):
    pass

class CargoTypeRead(CargoTypeBase):
    id: int

    class Config:
        orm_mode = True
