from pydantic import BaseModel
from typing import Optional


class CarrierInfoBase(BaseModel):
    name: str


class CarrierInfoCreate(CarrierInfoBase):
    pass


class CarrierInfoUpdate(BaseModel):
    name: Optional[str] = None


class CarrierInfoRead(CarrierInfoBase):
    id: int

    class Config:
        from_attributes = True
