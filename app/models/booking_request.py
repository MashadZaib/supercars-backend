# app/models/booking_request.py
from sqlalchemy import Column, Integer, String, Date, JSON
from app.core.database import Base
from sqlalchemy.orm import relationship

class BookingRequest(Base):
    __tablename__ = "booking_requests"

    id = Column(Integer, primary_key=True, index=True)
    requested_date = Column(Date, nullable=False)
    type_of_request = Column(String(50), nullable=False)
    booking_party = Column(String(255), nullable=False)
    user_id = Column(String(100), nullable=False)
    port_of_load = Column(String(100), nullable=False)
    port_of_discharge = Column(String(100), nullable=False)
    cargo_type = Column(String(100))
    container_size = Column(String(50))
    quantity = Column(String(50))
    hs_code = Column(String(50))
    weight_kg = Column(String(50))
    commodity = Column(String(255))
    shipping_lines = Column(JSON, nullable=True)
    confirmations = relationship("BookingConfirmation", back_populates="booking_request", cascade="all, delete")
    client_info = relationship("ClientInfo", back_populates="booking_request", cascade="all, delete")
    shipping_instructions = relationship("ShippingInstruction", back_populates="booking_request", cascade="all, delete")
    charges = relationship("Charge", back_populates="booking_request", cascade="all, delete")
    invoice_previews = relationship("InvoicePreview", back_populates="booking_request", cascade="all, delete")