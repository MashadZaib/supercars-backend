# app/schemas/invoice_preview_schema.py
from pydantic import BaseModel
from datetime import datetime
from typing import List, Dict, Any, Optional

class InvoicePreviewBase(BaseModel):
    bill_to: List[Dict[str, Any]]
    invoice_info: List[Dict[str, Any]]
    shipping_details: Optional[List[Dict[str, Any]]] = []
    container_details: Optional[List[Dict[str, Any]]] = []
    itemized_charges: Optional[List[Dict[str, Any]]] = []
    totals: Optional[Dict[str, Any]]

class InvoicePreviewCreate(InvoicePreviewBase):
    pass

class InvoicePreviewRead(InvoicePreviewBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
