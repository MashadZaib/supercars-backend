from pydantic import BaseModel, EmailStr
from typing import Optional

class ClientInfoBase(BaseModel):
    company_name: str
    contact_person: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    billing_address: Optional[str] = None
    shipping_address: Optional[str] = None
    country: Optional[str] = None
    city: Optional[str] = None
    postal_code: Optional[str] = None
    tax_id: Optional[str] = None
    registration_no: Optional[str] = None
    payment_terms: Optional[str] = None
    currency: Optional[str] = "USD"

class ClientInfoCreate(ClientInfoBase):
    """Used when creating new client info"""
    pass

class ClientInfoUpdate(BaseModel):
    """Used when updating existing client info"""
    company_name: Optional[str] = None
    contact_person: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    billing_address: Optional[str] = None
    shipping_address: Optional[str] = None
    country: Optional[str] = None
    city: Optional[str] = None
    postal_code: Optional[str] = None
    tax_id: Optional[str] = None
    registration_no: Optional[str] = None
    payment_terms: Optional[str] = None
    currency: Optional[str] = None

class ClientInfoRead(ClientInfoBase):
    id: int

    class Config:
        orm_mode = True
