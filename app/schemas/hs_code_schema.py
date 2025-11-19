from pydantic import BaseModel, Field
from typing import Optional

class HsCodeBase(BaseModel):
    name: Optional[str] = Field(None)
class HsCodeCreate(HsCodeBase):
    pass

class HsCodeRead(HsCodeBase):
    id: int

    class Config:
        from_attributes = True
