# app/models/charge.py
from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from app.core.database import Base

class Charge(Base):
    __tablename__ = "charges"

    id = Column(Integer, primary_key=True, index=True)
    invoice_id = Column(Integer, ForeignKey("invoice_previews.id", ondelete="CASCADE"))
    charge_name = Column(String(255), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False, default=0)
    qty = Column(Integer, default=1)
    type = Column(String(50), default="Taxable")

    invoice = relationship("InvoicePreview", back_populates="charges")
