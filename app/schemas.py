from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from typing import List

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_active: bool
    is_superuser: bool
    created_at: Optional[datetime]

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None


class BookingBase(BaseModel):
    # Many fields are optional because steps can be filled partially
    new_booking_instructions: Optional[str] = None
    date_received_from_client: Optional[datetime] = None
    method: Optional[str] = None
    client_name: Optional[str] = None
    client_address: Optional[str] = None
    client_email: Optional[str] = None
    client_contact_no: Optional[str] = None
    port_of_load: Optional[str] = None
    port_of_discharge: Optional[str] = None
    no_size_containers: Optional[str] = None
    number_of_vehicles: Optional[str] = None
    cy_details: Optional[str] = None
    freight_terms: Optional[str] = None
    bl_type: Optional[str] = None
    custom_broker_yard_name: Optional[str] = None
    bk_messrs_agent: Optional[str] = None

    new_booking_request_sent: Optional[datetime] = None
    file_reference: Optional[str] = None
    carrier_requested_date: Optional[datetime] = None
    container_release_from_depot: Optional[str] = None

    new_booking_request_received: Optional[datetime] = None
    rate_confirmed_monthly: Optional[str] = None
    booking_confirmation_received: Optional[datetime] = None
    booking_number: Optional[str] = None
    vessel_name: Optional[str] = None
    voyage: Optional[str] = None
    cy_cut_off: Optional[datetime] = None
    doc_cut_off: Optional[datetime] = None
    shipping_instruction_cut_off: Optional[datetime] = None

    new_booking_request_sent_to_client: Optional[datetime] = None
    rates_validity: Optional[str] = None
    booking_confirmation: Optional[datetime] = None
    booking_status: Optional[str] = None
    customs_doc_cut_off: Optional[datetime] = None
    shipping_instruction_cut_off_request: Optional[datetime] = None

    shipping_instructions: Optional[str] = None
    shipper_details: Optional[str] = None
    consignee_details: Optional[str] = None
    notify_details: Optional[str] = None
    marks_and_numbers: Optional[str] = None
    container_numbers: Optional[str] = None
    seal_numbers: Optional[str] = None
    vehicle_details: Optional[str] = None
    submits_shipping_instruction: Optional[datetime] = None

    draft_bl_shared_date: Optional[datetime] = None
    draft_bl_notes: Optional[str] = None
    draft_bl_sent_to_client_date: Optional[datetime] = None
    draft_bl_to_confirm: Optional[str] = None
    receive_draft_bl_confirmation: Optional[datetime] = None
    client_confirmation_notes: Optional[str] = None
    confirm_draft_bl_with_carrier_date: Optional[datetime] = None
    carrier_bl_ref: Optional[str] = None

    date_of_invoice: Optional[datetime] = None
    invoice_no: Optional[str] = None
    invoice_amount: Optional[float] = None
    due_date_for_payment: Optional[datetime] = None
    method_reference_of_payment: Optional[str] = None
    date_final_bl_released: Optional[datetime] = None

    status: Optional[str] = None
    method_of_payment: Optional[str] = None
    date_payment_received: Optional[datetime] = None
    amount_paid: Optional[float] = None
    amendment_requested: Optional[str] = None

    payment_to_shipping_line: Optional[float] = None
    date_of_payment: Optional[datetime] = None
    amount_of_payment: Optional[float] = None
    request_to_carrier_for_amendments: Optional[str] = None

    carrier_confirm_cargo_loaded: Optional[datetime] = None
    bl_ready: Optional[datetime] = None
    carizo_confirm_cargo_loaded: Optional[datetime] = None
    bl_ready_client: Optional[datetime] = None
    notify_client_amendment_charges: Optional[str] = None


class BookingCreate(BookingBase):
    pass


class BookingUpdate(BookingBase):
    pass


class BookingOut(BookingBase):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
