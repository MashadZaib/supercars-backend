# app/schemas/client_schema.py
from pydantic import BaseModel, EmailStr
from typing import Optional

class ClientBase(BaseModel):
    company_name: str
    contact_person: Optional[str]
    email: Optional[EmailStr]
    phone: Optional[str]
    address: Optional[str]
    tax_id: Optional[str]
    registration_no: Optional[str]

class ClientCreate(ClientBase):
    company_name: str

class ClientUpdate(BaseModel):
    company_name: Optional[str]
    contact_person: Optional[str]
    email: Optional[EmailStr]
    phone: Optional[str]
    address: Optional[str]
    tax_id: Optional[str]
    registration_no: Optional[str]

class ClientRead(ClientBase):
    id: int
    class Config:
        orm_mode = True
