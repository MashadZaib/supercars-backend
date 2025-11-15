from pydantic import BaseModel
from typing import Optional


class HsCodeBase(BaseModel):
    code: str
    description: Optional[str] = None


class HsCodeCreate(HsCodeBase):
    """Schema used for creating new HS Codes"""
    pass


class HsCodeUpdate(BaseModel):
    """Schema used for updating existing HS Codes"""
    code: Optional[str] = None
    description: Optional[str] = None


class HsCodeRead(HsCodeBase):
    id: int

    class Config:
        orm_mode = True
