from sqlalchemy import Column, Integer, JSON, DateTime, func
from sqlalchemy.orm import relationship
from app.core.database import Base

class InvoicePreview(Base):
    __tablename__ = "invoice_previews"

    id = Column(Integer, primary_key=True, index=True)
    bill_to = Column(JSON, nullable=False)
    invoice_info = Column(JSON, nullable=False)
    shipping_details = Column(JSON, nullable=True)
    container_details = Column(JSON, nullable=True)
    itemized_charges = Column(JSON, nullable=True)
    totals = Column(JSON, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # optional link to charges
    charges = relationship("Charge", back_populates="invoice_preview", cascade="all, delete-orphan")
