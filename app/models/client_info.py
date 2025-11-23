from sqlalchemy import Column, Integer, String, Date, Enum
from sqlalchemy.orm import relationship
from app.core.database import Base



class ClientInfo(Base):
    __tablename__ = "client_info"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=True)
    company_registration_no = Column(String(255), nullable=True)
    tax_id = Column(String(255), nullable=True)
    company_vat_no = Column(String(255), nullable=True)
    contact_person = Column(String(255), nullable=True)
    email = Column(String(255), nullable=True)
    phone = Column(String(50), nullable=True)
    address = Column(String(500), nullable=True)
    booking_requests = relationship(
        "BookingRequestClientInfo",
        back_populates="client_info",
        cascade="all, delete-orphan"
    )
