from pydantic import BaseModel, EmailStr
from datetime import date
from typing import List, Optional, Dict, Any

class PartyInfo(BaseModel):
    name: Optional[str]
    address: Optional[str]
    phone: Optional[str]
    contactPerson: Optional[str]
    email: Optional[EmailStr] = None

class VehicleInfo(BaseModel):
    make: Optional[str]
    year: Optional[str]
    color: Optional[str]
    chassisNo: Optional[str]
    length: Optional[str]
    width: Optional[str]
    height: Optional[str]
    m3: Optional[str]
    cc: Optional[str]

class MarksNumbers(BaseModel):
    containerNo: Optional[str]
    sealNo: Optional[str]
    size: Optional[str]
    type: Optional[str]
    noOfPackages: Optional[str]
    pkgType: Optional[str]
    cargoWeight: Optional[str]

class ShippingInstructionBase(BaseModel):
    type_of_bill_of_lading: Optional[str]
    shipper: Optional[PartyInfo]
    consignee: Optional[PartyInfo]
    notify: Optional[PartyInfo]
    vessel: Optional[str]
    voyage: Optional[str]
    booking_reference: Optional[str]
    bill_of_lading_no: Optional[str]
    port_of_load: Optional[str]
    port_of_discharge: Optional[str]
    etd_departure: Optional[date]
    eta_arrival: Optional[date]
    vehicles: Optional[List[VehicleInfo]] = []
    marks_numbers: Optional[List[MarksNumbers]] = []
    special_instructions: Optional[str]
    dangerous_goods: Optional[bool] = False
    temperature_control: Optional[str]
    humidity_control: Optional[str]

class ShippingInstructionCreate(ShippingInstructionBase):
    pass

class ShippingInstructionRead(ShippingInstructionBase):
    id: int
    class Config:
        orm_mode = True
