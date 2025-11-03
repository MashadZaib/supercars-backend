from pydantic import BaseModel
from datetime import date
from typing import Optional

class BookingConfirmationBase(BaseModel):
    carrier_name: str
    rates_confirmed: Optional[str] = None
    booking_confirmation_no: str
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

class BookingConfirmationCreate(BookingConfirmationBase):
    """Used for creating a new booking confirmation"""
    pass

class BookingConfirmationUpdate(BaseModel):
    """Used for updating a booking confirmation"""
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
