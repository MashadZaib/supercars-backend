from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from app.core.database import Base

class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id", ondelete="CASCADE"), nullable=False)
    description = Column(String(500), nullable=True)
    currency = Column(String(10), default="USD")
    amount = Column(Numeric(10, 2), nullable=False, default=0)

    client = relationship("Client", back_populates="invoices")
