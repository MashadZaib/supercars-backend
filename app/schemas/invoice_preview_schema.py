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
    """Schema used for creating a new invoice preview"""
    pass

class InvoicePreviewUpdate(BaseModel):
    """Schema used for updating an existing invoice preview"""
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
        orm_mode = True
