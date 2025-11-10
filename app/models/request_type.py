from sqlalchemy import Column, Integer, String
from app.core.database import Base

class RequestType(Base):
    __tablename__ = "request_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
