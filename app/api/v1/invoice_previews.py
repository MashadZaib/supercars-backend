from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.core.dependencies import db_session
from app.schemas.invoice_preview_schema import (
    InvoicePreviewCreate,
    InvoicePreviewRead,
    InvoicePreviewUpdate
)
from app.services.invoice_preview_service import InvoicePreviewService

router = APIRouter()

@router.post("/", response_model=InvoicePreviewRead, status_code=status.HTTP_201_CREATED)
def create_invoice_preview(payload: InvoicePreviewCreate, db: Session = Depends(db_session)):
    return InvoicePreviewService(db).create_preview(payload)

@router.get("/", response_model=List[InvoicePreviewRead])
def list_invoice_previews(db: Session = Depends(db_session)):
    return InvoicePreviewService(db).list_previews()

@router.get("/{preview_id}", response_model=InvoicePreviewRead)
def get_invoice_preview(preview_id: int, db: Session = Depends(db_session)):
    preview = InvoicePreviewService(db).get_preview(preview_id)
    if not preview:
        raise HTTPException(status_code=404, detail="Invoice preview not found")
    return preview

@router.put("/{preview_id}", response_model=InvoicePreviewRead)
def update_invoice_preview(preview_id: int, payload: InvoicePreviewUpdate, db: Session = Depends(db_session)):
    updated = InvoicePreviewService(db).update_preview(preview_id, payload)
    if not updated:
        raise HTTPException(status_code=404, detail="Invoice preview not found")
    return updated

@router.delete("/{preview_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_invoice_preview(preview_id: int, db: Session = Depends(db_session)):
    ok = InvoicePreviewService(db).delete_preview(preview_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Invoice preview not found")
    return None
