from pydantic import BaseModel
from datetime import date
from typing import Optional

class BookingConfirmationBase(BaseModel):
    carrier_name: str
    rates_confirmed: Optional[str]
    booking_confirmation_no: str
    booking_date: Optional[date]
    shipper: Optional[str]
    port_of_load: Optional[str]
    port_of_discharge: Optional[str]
    vessel_name: Optional[str]
    voyage: Optional[str]
    container_size: Optional[str]
    quantity: Optional[str]
    weight_kg: Optional[str]
    cy_cfs: Optional[str]
    hs_code: Optional[str]
    cargo_description: Optional[str]

class BookingConfirmationCreate(BookingConfirmationBase):
    pass

class BookingConfirmationRead(BookingConfirmationBase):
    id: int
    class Config:
        orm_mode = True
