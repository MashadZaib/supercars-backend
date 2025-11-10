from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class BookingConfirmationBase(BaseModel):
    booking_request_id: int = Field(..., description="Linked Booking Request ID")
    carrier_name: str
    rates_confirmed: Optional[str] = None
    booking_confirmation_no: str
    booking_date: Optional[date] = None
    shipper_id: Optional[int] = None
    port_of_load_id: Optional[int] = None
    port_of_discharge_id: Optional[int] = None
    vessel_id: Optional[int] = None
    voyage: Optional[str] = None
    container_size: Optional[str] = None
    quantity: Optional[str] = None
    weight_kg: Optional[str] = None
    cy_cfs: Optional[str] = None
    hs_code_id: Optional[int] = None
    cargo_description_id: Optional[int] = None

class BookingConfirmationCreate(BookingConfirmationBase):
    pass

class BookingConfirmationUpdate(BaseModel):
    carrier_name: Optional[str] = None
    rates_confirmed: Optional[str] = None
    booking_confirmation_no: Optional[str] = None
    booking_date: Optional[date] = None
    shipper: Optional[str] = None
    port_of_load: Optional[str] = None
    port_of_discharge: Optional[str] = None
    vessel_name: Optional[str] = None
    voyage: Optional[str] = None
    container_size: Optional[str] = None
    quantity: Optional[str] = None
    weight_kg: Optional[str] = None
    cy_cfs: Optional[str] = None
    hs_code: Optional[str] = None
    cargo_description: Optional[str] = None

class BookingConfirmationRead(BookingConfirmationBase):
    id: int

    class Config:
        orm_mode = True
