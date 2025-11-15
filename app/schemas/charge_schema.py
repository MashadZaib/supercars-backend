from pydantic import BaseModel, condecimal, Field
from typing import Optional

class ChargeBase(BaseModel):
    booking_request_id: int = Field(..., description="Linked Booking Request ID")
    charge_name: str
    currency: str = "USD"
    amount: condecimal(max_digits=10, decimal_places=2)
    quantity: int = 1
    taxable: Optional[str] = "False"
    tax_rate: Optional[condecimal(max_digits=5, decimal_places=2)] = 0
    notes: Optional[str] = None

class ChargeCreate(ChargeBase):
    invoice_preview_id: int

class ChargeUpdate(BaseModel):
    charge_name: Optional[str] = None
    currency: Optional[str] = None
    amount: Optional[condecimal(max_digits=10, decimal_places=2)] = None
    quantity: Optional[int] = None
    taxable: Optional[str] = None
    tax_rate: Optional[condecimal(max_digits=5, decimal_places=2)] = None
    notes: Optional[str] = None

class ChargeRead(ChargeBase):
    id: int
    invoice_preview_id: int

    class Config:
        orm_mode = True
