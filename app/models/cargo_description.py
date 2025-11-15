from sqlalchemy import Column, Integer, String, Text
from app.core.database import Base

class CargoDescription(Base):
    __tablename__ = "cargo_descriptions"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(Text, nullable=False)
