from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class PortBase(BaseModel):
    name: Optional[str] = Field(None)
    type: Optional[str] = Field(None)
class PortCreate(PortBase):
    pass

class PortRead(PortBase):
    id: int

    class Config:
        from_attributes = True
