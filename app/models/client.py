from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String(255), nullable=False)
    contact_person = Column(String(255), nullable=True)
    email = Column(String(255), nullable=True, unique=True)
    phone = Column(String(50), nullable=True)
    billing_address = Column(String(500), nullable=True)
    shipping_address = Column(String(500), nullable=True)
    country = Column(String(100), nullable=True)
    city = Column(String(100), nullable=True)
    postal_code = Column(String(50), nullable=True)
    tax_id = Column(String(100), nullable=True)
    registration_no = Column(String(100), nullable=True)
    payment_terms = Column(String(100), nullable=True)
    currency = Column(String(10), nullable=True, default="USD")
