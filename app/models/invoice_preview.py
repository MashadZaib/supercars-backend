# app/models/invoice_preview.py
from sqlalchemy import Column, Integer, JSON, DateTime, func
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
