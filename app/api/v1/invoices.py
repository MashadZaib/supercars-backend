from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from app.core.dependencies import db_session
from app.schemas.invoice_schema import InvoiceCreate, InvoiceRead, InvoiceUpdate
from app.services.invoice_service import InvoiceService

router = APIRouter()

@router.post("/", response_model=InvoiceRead, status_code=status.HTTP_201_CREATED)
def create_invoice(payload: InvoiceCreate, db: Session = Depends(db_session)):
    return InvoiceService(db).create_invoice(payload)

@router.get("/", response_model=List[InvoiceRead])
def list_invoices(db: Session = Depends(db_session)):
    return InvoiceService(db).list_invoices()

@router.get("/{invoice_id}", response_model=InvoiceRead)
def get_invoice(invoice_id: int, db: Session = Depends(db_session)):
    inv = InvoiceService(db).get_invoice(invoice_id)
    if not inv:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return inv

@router.put("/{invoice_id}", response_model=InvoiceRead)
def update_invoice(invoice_id: int, payload: InvoiceUpdate, db: Session = Depends(db_session)):
    inv = InvoiceService(db).update_invoice(invoice_id, payload)
    if not inv:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return inv

@router.delete("/{invoice_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_invoice(invoice_id: int, db: Session = Depends(db_session)):
    ok = InvoiceService(db).delete_invoice(invoice_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return None
