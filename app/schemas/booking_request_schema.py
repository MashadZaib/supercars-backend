from pydantic import BaseModel, Field
from datetime import date
from typing import List, Optional

class ShippingLine(BaseModel):
    carrier: str
    date_sent: Optional[str] = Field(None, alias="dateSent")
    method: Optional[str] = None
    confirmation_id: Optional[str] = Field(None, alias="confirmationId")
    status: Optional[str] = None
    freight: Optional[str] = None

    class Config:
        allow_population_by_field_name = True  # ✅ accepts both dateSent and date_sent

class BookingRequestBase(BaseModel):
    requested_date: date
    type_of_request: str
    booking_party: str
    user_id: str
    port_of_load: str
    port_of_discharge: str
    cargo_type: Optional[str] = None
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
    type_of_request: Optional[str] = None
    booking_party: Optional[str] = None
    user_id: Optional[str] = None
    port_of_load: Optional[str] = None
    port_of_discharge: Optional[str] = None
    cargo_type: Optional[str] = None
    container_size: Optional[str] = None
    quantity: Optional[str] = None
    hs_code: Optional[str] = None
    weight_kg: Optional[str] = None
    commodity: Optional[str] = None
    shipping_lines: Optional[List[ShippingLine]] = []

class BookingRequestRead(BookingRequestBase):
    id: int

    class Config:
        orm_mode = True
