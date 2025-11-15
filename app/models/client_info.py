from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class ClientInfo(Base):
    __tablename__ = "client_info"

    id = Column(Integer, primary_key=True, index=True)
    company_registration_no = Column(String(255), nullable=True)
    tax_id = Column(String(255), nullable=True)
    company_vat_no = Column(String(255), nullable=True)
    contact_person = Column(String(255))
    email = Column(String(255))
    phone = Column(String(50))
    billing_address = Column(String(500))
    shipping_address = Column(String(500))

    # ✅ Link to booking request
    booking_request_id = Column(Integer, ForeignKey("booking_requests.id", ondelete="CASCADE"))
    booking_request = relationship("BookingRequest", back_populates="client_info")
