# app/schemas/charge_schema.py
from pydantic import BaseModel, condecimal
from typing import Optional

class ChargeBase(BaseModel):
    charge_name: str
    amount: condecimal(max_digits=10, decimal_places=2)
    qty: int = 1
    type: str = "Taxable"

class ChargeCreate(ChargeBase):
    invoice_id: int

class ChargeUpdate(BaseModel):
    charge_name: Optional[str]
    amount: Optional[condecimal(max_digits=10, decimal_places=2)]
    qty: Optional[int]
    type: Optional[str]

class ChargeRead(ChargeBase):
    id: int
    invoice_id: int

    class Config:
        orm_mode = True
