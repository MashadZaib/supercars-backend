from sqlalchemy import Column, Integer, String, Date, JSON, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import date
class BookingRequest(Base):
    __tablename__ = "booking_requests"

    id = Column(Integer, primary_key=True, index=True)
    requested_date = Column(Date, nullable=False, default=date.today)

    # Foreign Keys
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    type_of_request_id = Column(Integer, ForeignKey("request_types.id"), nullable=False)
    booking_party_id = Column(Integer, ForeignKey("booking_parties.id"), nullable=False)
    port_of_load_id = Column(Integer, ForeignKey("ports.id"), nullable=False)
    port_of_discharge_id = Column(Integer, ForeignKey("ports.id"), nullable=False)
    cargo_type_id = Column(Integer, ForeignKey("cargo_types.id"), nullable=True)
    container_size_id = Column(Integer, ForeignKey("container_sizes.id"), nullable=True)
    hs_code_id = Column(Integer, ForeignKey("hs_codes.id"), nullable=True)
    # Relationships
    request_type = relationship("RequestType")
    user = relationship("User")
    booking_party = relationship("BookingParty", back_populates="booking_requests")
    port_of_load = relationship("Port", foreign_keys=[port_of_load_id])
    port_of_discharge = relationship("Port", foreign_keys=[port_of_discharge_id])
    cargo_type = relationship("CargoType")
    container_size = relationship("ContainerSize")
    hs_code = relationship("HsCode")
    quantity = Column(String(50))
    weight_kg = Column(String(50))
    commodity = Column(String(255))
    shipping_lines = Column(JSON, nullable=True)

    # Relationships with other models
    confirmations = relationship("BookingConfirmation", back_populates="booking_request", cascade="all, delete")
    client_infos = relationship(
        "BookingRequestClientInfo",
        back_populates="booking_request",
        cascade="all, delete-orphan"
    )
    shipping_instructions = relationship("ShippingInstruction", back_populates="booking_request", cascade="all, delete")
    charges = relationship("Charge", back_populates="booking_request", cascade="all, delete")
    invoice_previews = relationship("InvoicePreview", back_populates="booking_request", cascade="all, delete")
    
