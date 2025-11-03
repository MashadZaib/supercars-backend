from sqlalchemy import Column, Integer, String, Boolean, Date, JSON
from app.core.database import Base

class ShippingInstruction(Base):
    __tablename__ = "shipping_instructions"

    id = Column(Integer, primary_key=True, index=True)
    type_of_bill_of_lading = Column(String(50))
    shipper = Column(JSON)
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
