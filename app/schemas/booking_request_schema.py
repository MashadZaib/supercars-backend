from pydantic import BaseModel
from datetime import date
from typing import List, Optional, Dict, Any

class ShippingLine(BaseModel):
    carrier: str
    dateSent: Optional[str]
    method: Optional[str]
    confirmationId: Optional[str]
    status: Optional[str]
    freight: Optional[str]

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
    pass

class BookingRequestRead(BookingRequestBase):
    id: int
    class Config:
        orm_mode = True
