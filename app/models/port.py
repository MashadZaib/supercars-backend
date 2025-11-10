from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Port(Base):
    __tablename__ = "ports"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    type = Column(String(50), nullable=False)  # e.g. "load" or "discharge"
