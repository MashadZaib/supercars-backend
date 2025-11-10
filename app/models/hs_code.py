from sqlalchemy import Column, Integer, String
from app.core.database import Base

class HsCode(Base):
    __tablename__ = "hs_codes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
