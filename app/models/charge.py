from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Charge(Base):
    __tablename__ = "charges"

    id = Column(Integer, primary_key=True, index=True)
    invoice_preview_id = Column(Integer, ForeignKey("invoice_previews.id", ondelete="CASCADE"))
    charge_name = Column(String(255), nullable=False)
    currency = Column(String(10), default="USD")
    amount = Column(Numeric(10, 2), nullable=False, default=0)
    quantity = Column(Integer, default=1)
    taxable = Column(String(5), default="False")
    tax_rate = Column(Numeric(5, 2), default=0)
    notes = Column(String(500), nullable=True)

    invoice_preview = relationship("InvoicePreview", back_populates="charges")
    booking_request_id = Column(Integer, ForeignKey("booking_requests.id", ondelete="CASCADE"))
    booking_request = relationship("BookingRequest", back_populates="charges")