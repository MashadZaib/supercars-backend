from sqlalchemy import Column, Integer, String, Boolean, Date, JSON, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
from typing import Optional
class ShippingInstruction(Base):
    __tablename__ = "shipping_instructions"

    id = Column(Integer, primary_key=True, index=True)
    type_of_bill_of_lading = Column(String(50))
    shipper_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    consignee = Column(JSON)
    notify = Column(JSON)
    vessel = Column(String(255))
    voyage = Column(String(100))
    booking_reference = Column(String(100))
    bill_of_lading_no = Column(String(100))
    port_of_load = Column(String(100))
    port_of_discharge = Column(String(100))
    etd_departure = Column(Date)
    eta_arrival = Column(Date)
    vehicles = Column(JSON)
    marks_numbers = Column(JSON)
    special_instructions = Column(String(1000))
    dangerous_goods = Column(Boolean, default=False)
    temperature_control = Column(String(50))
    humidity_control = Column(String(50))
    booking_request_id = Column(Integer, ForeignKey("booking_requests.id", ondelete="CASCADE"))
    booking_request = relationship("BookingRequest", back_populates="shipping_instructions")
    user = relationship("User", foreign_keys=[shipper_id])