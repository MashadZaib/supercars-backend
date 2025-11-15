from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class ClientInfoBase(BaseModel):
    booking_request_id: int = Field(..., description="Linked Booking Request ID")
    contact_person: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    billing_address: Optional[str] = None
    shipping_address: Optional[str] = None
    tax_id: Optional[str] = None
    company_registration_no: Optional[str] = None

class ClientInfoCreate(ClientInfoBase):
    """Used when creating new client info"""
    pass

class ClientInfoUpdate(BaseModel):
    """Used when updating existing client info"""
    contact_person: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    billing_address: Optional[str] = None
    shipping_address: Optional[str] = None
    tax_id: Optional[str] = None
    company_registration_no: Optional[str] = None

class ClientInfoRead(ClientInfoBase):
    id: int

    class Config:
        orm_mode = True
