from pydantic import BaseModel
from typing import Optional


class VesselInfoBase(BaseModel):
    name: str


class VesselInfoCreate(VesselInfoBase):
    pass


class VesselInfoUpdate(BaseModel):
    name: Optional[str] = None


class VesselInfoRead(VesselInfoBase):
    id: int

    class Config:
        from_attributes = True
