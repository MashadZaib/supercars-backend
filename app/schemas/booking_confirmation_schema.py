from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class BookingConfirmationBase(BaseModel):
    booking_request_id: int = Field(..., description="Linked Booking Request ID")
    carrier_id: Optional[int] = None
    rates_confirmed: Optional[str] = None
    booking_confirmation_no: str
    booking_date: Optional[date] = None
    shipper_id: Optional[int] = None
    port_of_load_id: Optional[int] = None
    port_of_discharge_id: Optional[int] = None
    vessel_id: Optional[int] = None
    voyage: Optional[str] = None
    container_size_id: Optional[int] = None
    quantity: Optional[str] = None
    weight_kg: Optional[str] = None
    cy_cfs: Optional[str] = None
    hs_code_id: Optional[int] = None
    cargo_description_id: Optional[int] = None

class BookingConfirmationCreate(BookingConfirmationBase):
    pass

class BookingConfirmationUpdate(BaseModel):
    carrier_id: Optional[int] = None
    rates_confirmed: Optional[str] = None
    booking_confirmation_no: Optional[str] = None
    booking_date: Optional[date] = None
    shipper_id: Optional[int] = None
    port_of_load_id: Optional[int] = None
    port_of_discharge_id: Optional[int] = None
    vessel_id: Optional[int] = None
    voyage: Optional[str] = None
    container_size_id: Optional[int] = None
    quantity: Optional[str] = None
    weight_kg: Optional[str] = None
    cy_cfs: Optional[str] = None
    hs_code_id: Optional[int] = None
    cargo_description_id: Optional[int] = None

class BookingConfirmationRead(BookingConfirmationBase):
    id: int

    class Config:
        from_attributes = True
