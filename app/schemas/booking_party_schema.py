from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class BookingPartyBase(BaseModel):
    name: Optional[str] = Field(None, example="ACME Logistics")
    address: Optional[str] = Field(None, example="123 Shipping Lane, Dubai, UAE")
    email: Optional[EmailStr] = Field(None, example="info@acme.com")
    phone: Optional[str] = Field(None, example="+971500000000")
class BookingPartyCreate(BookingPartyBase):
    pass

class BookingPartyRead(BookingPartyBase):
    id: int

    class Config:
        from_attributes = True
