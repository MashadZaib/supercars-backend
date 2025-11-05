from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class BookingPartyBase(BaseModel):
    name: str = Field(..., example="ACME Logistics")
    address: str = Field(..., example="123 Shipping Lane, Dubai, UAE")
    contact_email: Optional[EmailStr] = Field(None, example="info@acme.com")

class BookingPartyCreate(BookingPartyBase):
    pass

class BookingPartyRead(BookingPartyBase):
    id: int

    class Config:
        orm_mode = True
