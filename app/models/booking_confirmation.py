from sqlalchemy import Column, Integer, String, Date
from app.core.database import Base

class BookingConfirmation(Base):
    __tablename__ = "booking_confirmations"

    id = Column(Integer, primary_key=True, index=True)
    carrier_name = Column(String(100), nullable=False)
    rates_confirmed = Column(String(255))
    booking_confirmation_no = Column(String(100), nullable=False)
    booking_date = Column(Date)
    shipper = Column(String(255))
    port_of_load = Column(String(100))
    port_of_discharge = Column(String(100))
    vessel_name = Column(String(255))
    voyage = Column(String(100))
    container_size = Column(String(50))
    quantity = Column(String(50))
    weight_kg = Column(String(50))
    cy_cfs = Column(String(100))
    hs_code = Column(String(50))
    cargo_description = Column(String(255))
