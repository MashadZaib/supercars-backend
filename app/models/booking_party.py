from sqlalchemy import Column, Integer, String, Text
from app.core.database import Base

class BookingParty(Base):
    __tablename__ = "booking_parties"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=True)
    address = Column(Text, nullable=True)

