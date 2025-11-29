from pydantic import BaseModel, EmailStr, Field
from datetime import date
from typing import List, Optional, Dict, Any

class PartyInfo(BaseModel):
    name: Optional[str]
    address: Optional[str]
    phone: Optional[str]
    contact_person: Optional[str]
    email: Optional[EmailStr] = None

class VehicleInfo(BaseModel):
    make: Optional[str]
    year: Optional[str]
    color: Optional[str]
    chassis_no: Optional[str]
    length: Optional[str]
    width: Optional[str]
    height: Optional[str]
    m3: Optional[str]
    cc: Optional[str]

class MarksNumbers(BaseModel):
    container_no: Optional[str]
    seal_no: Optional[str]
    size: Optional[str]
    type: Optional[str]
    no_of_packages: Optional[str]
    pkg_type: Optional[str]
    cargo_weight: Optional[str]

class ShippingInstructionBase(BaseModel):
    booking_request_id: int = Field(..., description="Linked Booking Request ID")
    type_of_bill_of_lading: Optional[str]
    shipper_id: Optional[int] = None
    consignee: Optional[Dict[str, Any]] = None
    notify: Optional[Dict[str, Any]] = None
    vessel: Optional[str]
    voyage: Optional[str]
    booking_reference: Optional[str]
    bill_of_lading_no: Optional[str]
    port_of_load: Optional[str]
    port_of_discharge: Optional[str]
    etd_departure: Optional[date]
    eta_arrival: Optional[date]
    vehicles: Optional[List[Dict[str, Any]]] = []
    marks_numbers: Optional[List[Dict[str, Any]]] = []
    special_instructions: Optional[str]
    dangerous_goods: Optional[bool] = False
    temperature_control: Optional[str]
    humidity_control: Optional[str]

class ShippingInstructionCreate(ShippingInstructionBase):
    pass

class ShippingInstructionUpdate(BaseModel):
    type_of_bill_of_lading: Optional[str] = None
    shipper_id: Optional[int] = None
    consignee: Optional[Dict[str, Any]] = None
    notify: Optional[Dict[str, Any]] = None
    vessel: Optional[str] = None
    voyage: Optional[str] = None
    booking_reference: Optional[str] = None
    bill_of_lading_no: Optional[str] = None
    port_of_load: Optional[str] = None
    port_of_discharge: Optional[str] = None
    etd_departure: Optional[date] = None
    eta_arrival: Optional[date] = None
    vehicles: Optional[List[Dict[str, Any]]] = None
    marks_numbers: Optional[List[Dict[str, Any]]] = None
    special_instructions: Optional[str] = None
    dangerous_goods: Optional[bool] = None
    temperature_control: Optional[str] = None
    humidity_control: Optional[str] = None

class ShippingInstructionRead(ShippingInstructionBase):
    id: int

    class Config:
        from_attributes = True
