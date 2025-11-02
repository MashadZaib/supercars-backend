from pydantic import BaseModel, condecimal
from typing import Optional

class InvoiceBase(BaseModel):
    client_id: int
    description: Optional[str] = None
    currency: str = "USD"
    amount: condecimal(max_digits=10, decimal_places=2) = 0

class InvoiceCreate(InvoiceBase):
    pass

class InvoiceUpdate(BaseModel):
    description: Optional[str] = None
    currency: Optional[str] = None
    amount: Optional[condecimal(max_digits=10, decimal_places=2)] = None

class InvoiceRead(InvoiceBase):
    id: int

    class Config:
        orm_mode = True
