from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.core.database import Base
from sqlalchemy.orm import relationship

class BookingConfirmation(Base):
    __tablename__ = "booking_confirmations"

    id = Column(Integer, primary_key=True, index=True)
    carrier_id = Column(Integer, ForeignKey("carrier_info.id"), nullable=False)
    rates_confirmed = Column(String(255))
    booking_confirmation_no = Column(String(100), nullable=False)
    booking_date = Column(Date)
    shipper_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    port_of_load_id = Column(Integer, ForeignKey("ports.id"), nullable=False)
    port_of_discharge_id = Column(Integer, ForeignKey("ports.id"), nullable=False)
    vessel_id = Column(Integer, ForeignKey("vessel_info.id"), nullable=False)
    voyage = Column(String(100))
    container_size_id = Column(Integer, ForeignKey("container_sizes.id"), nullable=True)
    quantity = Column(String(50))
    weight_kg = Column(String(50))
    cy_cfs = Column(String(100))
    hs_code_id = Column(Integer, ForeignKey("hs_codes.id"), nullable=True)
    cargo_description_id = Column(Integer, ForeignKey("cargo_descriptions.id"), nullable=True)
    booking_request_id = Column(Integer, ForeignKey("booking_requests.id", ondelete="CASCADE"))
    
    
    user = relationship("User")
    port_of_load = relationship("Port", foreign_keys=[port_of_load_id])
    port_of_discharge = relationship("Port", foreign_keys=[port_of_discharge_id])
    carrier = relationship("CarrierInfo", foreign_keys=[carrier_id])
    vessel = relationship("VesselInfo", foreign_keys=[vessel_id])
    container_size = relationship("ContainerSize", foreign_keys=[container_size_id])
    hs_code = relationship("HsCode")
    cargo_description = relationship("CargoDescription", foreign_keys=[cargo_description_id])
    
    
    
    
    
    
    
    
    

    # ✅ Relationship back to BookingRequest
    booking_request = relationship("BookingRequest", back_populates="confirmations")