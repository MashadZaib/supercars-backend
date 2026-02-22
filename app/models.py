from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, Date, Float, func
from .database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(150), unique=True, index=True, nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Booking(Base):
    __tablename__ = 'bookings'
    id = Column(Integer, primary_key=True, index=True)
    # timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Step 1
    new_booking_instructions = Column(Text, nullable=True)
    date_received_from_client = Column(Date, nullable=True)
    method = Column(String(255), nullable=True)
    client_name = Column(String(255), nullable=True)
    client_address = Column(Text, nullable=True)
    client_email = Column(String(255), nullable=True)
    client_contact_no = Column(String(100), nullable=True)
    port_of_load = Column(String(255), nullable=True)
    port_of_discharge = Column(String(255), nullable=True)
    no_size_containers = Column(String(255), nullable=True)
    number_of_vehicles = Column(String(255), nullable=True)
    cy_details = Column(Text, nullable=True)
    freight_terms = Column(String(255), nullable=True)
    bl_type = Column(String(255), nullable=True)
    custom_broker_yard_name = Column(String(255), nullable=True)
    bk_messrs_agent = Column(String(255), nullable=True)

    # Step 2
    new_booking_request_sent = Column(Date, nullable=True)
    file_reference = Column(String(255), nullable=True)
    carrier_requested_date = Column(Date, nullable=True)
    container_release_from_depot = Column(String(255), nullable=True)

    # Step 3 / 4
    new_booking_request_received = Column(Date, nullable=True)
    rate_confirmed_monthly = Column(String(255), nullable=True)
    booking_confirmation_received = Column(Date, nullable=True)
    booking_number = Column(String(255), nullable=True)
    vessel_name = Column(String(255), nullable=True)
    voyage = Column(String(255), nullable=True)
    cy_cut_off = Column(DateTime, nullable=True)
    doc_cut_off = Column(DateTime, nullable=True)
    shipping_instruction_cut_off = Column(DateTime, nullable=True)
    new_booking_request_sent_to_client = Column(Date, nullable=True)
    rates_validity = Column(String(255), nullable=True)
    booking_confirmation = Column(Date, nullable=True)
    booking_status = Column(String(255), nullable=True)
    customs_doc_cut_off = Column(DateTime, nullable=True)
    shipping_instruction_cut_off_request = Column(DateTime, nullable=True)

    # Step 5 / 6
    shipping_instructions = Column(Text, nullable=True)
    shipper_details = Column(Text, nullable=True)
    consignee_details = Column(Text, nullable=True)
    notify_details = Column(Text, nullable=True)
    marks_and_numbers = Column(Text, nullable=True)
    container_numbers = Column(Text, nullable=True)
    seal_numbers = Column(Text, nullable=True)
    vehicle_details = Column(Text, nullable=True)
    submits_shipping_instruction = Column(Date, nullable=True)

    # Step 7-10
    draft_bl_shared_date = Column(Date, nullable=True)
    draft_bl_notes = Column(Text, nullable=True)
    draft_bl_sent_to_client_date = Column(Date, nullable=True)
    draft_bl_to_confirm = Column(Text, nullable=True)
    receive_draft_bl_confirmation = Column(Date, nullable=True)
    client_confirmation_notes = Column(Text, nullable=True)
    confirm_draft_bl_with_carrier_date = Column(Date, nullable=True)
    carrier_bl_ref = Column(String(255), nullable=True)

    # Invoice / Payment fields
    date_of_invoice = Column(Date, nullable=True)
    invoice_no = Column(String(255), nullable=True)
    invoice_amount = Column(Float, nullable=True)
    due_date_for_payment = Column(Date, nullable=True)
    method_reference_of_payment = Column(String(255), nullable=True)
    date_final_bl_released = Column(Date, nullable=True)

    status = Column(String(255), nullable=True)
    method_of_payment = Column(String(255), nullable=True)
    date_payment_received = Column(Date, nullable=True)
    amount_paid = Column(Float, nullable=True)
    amendment_requested = Column(Text, nullable=True)

    payment_to_shipping_line = Column(Float, nullable=True)
    date_of_payment = Column(Date, nullable=True)
    amount_of_payment = Column(Float, nullable=True)
    request_to_carrier_for_amendments = Column(Text, nullable=True)

    carrier_confirm_cargo_loaded = Column(Date, nullable=True)
    bl_ready = Column(Date, nullable=True)
    carizo_confirm_cargo_loaded = Column(Date, nullable=True)
    bl_ready_client = Column(Date, nullable=True)
    notify_client_amendment_charges = Column(Text, nullable=True)
