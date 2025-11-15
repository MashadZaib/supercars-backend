from sqlalchemy import Column, Integer, String
from app.core.database import Base

class VesselInfo(Base):
    __tablename__ = "vessel_info"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
