from pydantic import BaseModel, Field
from datetime import date
from typing import List, Optional

class ShippingLine(BaseModel):
    carrier: str
    date_sent: Optional[str] = None
    method: Optional[str] = None
    confirmation_id: Optional[str] = None
    status: Optional[str] = None
    freight: Optional[str] = None

class BookingRequestBase(BaseModel):
    requested_date: date
    type_of_request: str
    booking_party_id: int  # ✅ No alias - use snake_case
    user_id: str
    port_of_load_id: int  # ✅ No alias - use snake_case
    port_of_discharge_id: int  # ✅ No alias - use snake_case
    cargo_type_id: Optional[int] = None  # ✅ No alias - use snake_case
    container_size: Optional[str] = None
    quantity: Optional[str] = None
    hs_code: Optional[str] = None
    weight_kg: Optional[str] = None
    commodity: Optional[str] = None
    shipping_lines: Optional[List[ShippingLine]] = []

class BookingRequestCreate(BookingRequestBase):
    """Schema used for creating new booking requests"""
    pass

class BookingRequestUpdate(BaseModel):
    """Schema used for updating existing booking requests"""
    requested_date: Optional[date] = None
    type_of_request_id: Optional[int] = None
    booking_party_id: Optional[int] = None
    user_id: Optional[int] = None
    port_of_load_id: Optional[int] = None
    port_of_discharge_id: Optional[int] = None
    cargo_type_id: Optional[int] = None
    container_size_id: Optional[int] = None
    quantity: Optional[str] = None
    hs_code_id: Optional[int] = None
    weight_kg: Optional[str] = None
    commodity: Optional[str] = None
    shipping_lines: Optional[List[ShippingLine]] = []

class BookingRequestRead(BookingRequestBase):
    id: int

    class Config:
        orm_mode = True