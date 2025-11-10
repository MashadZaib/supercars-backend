from sqlalchemy import Column, Integer, String
from app.core.database import Base

class CargoType(Base):
    __tablename__ = "cargo_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
