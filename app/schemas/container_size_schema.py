from pydantic import BaseModel
from typing import Optional


class ContainerSizeBase(BaseModel):
    name: str


class ContainerSizeCreate(ContainerSizeBase):
    pass


class ContainerSizeUpdate(BaseModel):
    name: Optional[str] = None


class ContainerSizeRead(ContainerSizeBase):
    id: int

    class Config:
        from_attributes = True
