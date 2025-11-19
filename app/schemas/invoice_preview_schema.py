from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Dict, Any, Optional

class InvoicePreviewBase(BaseModel):
    booking_request_id: int = Field(..., description="Linked Booking Request ID")
    bill_to: List[Dict[str, Any]]
    invoice_info: List[Dict[str, Any]]
    shipping_details: Optional[List[Dict[str, Any]]] = []
    container_details: Optional[List[Dict[str, Any]]] = []
    itemized_charges: Optional[List[Dict[str, Any]]] = []
    totals: Optional[Dict[str, Any]] = None

class InvoicePreviewCreate(InvoicePreviewBase):
    pass

class InvoicePreviewUpdate(BaseModel):
    bill_to: Optional[List[Dict[str, Any]]] = None
    invoice_info: Optional[List[Dict[str, Any]]] = None
    shipping_details: Optional[List[Dict[str, Any]]] = None
    container_details: Optional[List[Dict[str, Any]]] = None
    itemized_charges: Optional[List[Dict[str, Any]]] = None
    totals: Optional[Dict[str, Any]] = None

class InvoicePreviewRead(InvoicePreviewBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
