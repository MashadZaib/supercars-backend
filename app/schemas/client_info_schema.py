from pydantic import BaseModel, EmailStr
from typing import Optional, List


class ClientInfoBase(BaseModel):
    name: Optional[str] = None
    contact_person: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    tax_id: Optional[str] = None
    company_registration_no: Optional[str] = None
    company_vat_no: Optional[str] = None


class ClientInfoCreate(ClientInfoBase):
    """Used when creating new client info"""
    pass


class ClientInfoUpdate(BaseModel):
    """Used when updating existing client info"""
    name: Optional[str] = None
    contact_person: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    tax_id: Optional[str] = None
    company_registration_no: Optional[str] = None
    company_vat_no: Optional[str] = None


class ClientInfoRead(ClientInfoBase):
    id: int
    # Optional: list of linked booking request IDs
    booking_request_ids: Optional[List[int]] = None

    class Config:
        from_attributes = True
