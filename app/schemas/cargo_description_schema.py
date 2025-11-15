from pydantic import BaseModel
from typing import Optional


class CargoDescriptionBase(BaseModel):
    description: str


class CargoDescriptionCreate(CargoDescriptionBase):
    pass


class CargoDescriptionUpdate(BaseModel):
    description: Optional[str] = None


class CargoDescriptionRead(CargoDescriptionBase):
    id: int

    class Config:
        orm_mode = True
