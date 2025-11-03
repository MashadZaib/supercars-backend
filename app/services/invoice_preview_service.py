from typing import List, Optional
from sqlalchemy.orm import Session
from app.schemas.invoice_preview_schema import InvoicePreviewCreate, InvoicePreviewUpdate
from app.models.invoice_preview import InvoicePreview
from app.repositories.invoice_repository import InvoiceRepository

class InvoiceService:
    def __init__(self, db: Session):
        self.repo = InvoiceRepository(db)

    def create_invoice(self, payload: InvoicePreviewCreate) -> InvoicePreview:
        obj = InvoicePreview(**payload.dict())
        return self.repo.create(obj)

    def list_invoices(self) -> List[InvoicePreview]:
        return self.repo.list()

    def get_invoice(self, invoice_id: int) -> Optional[InvoicePreview]:
        return self.repo.get(invoice_id)

    def update_invoice(self, invoice_id: int, payload: InvoicePreviewUpdate) -> Optional[InvoicePreview]:
        obj = self.repo.get(invoice_id)
        if not obj:
            return None
        return self.repo.update(obj, **payload.dict(exclude_unset=True))

    def delete_invoice(self, invoice_id: int) -> bool:
        obj = self.repo.get(invoice_id)
        if not obj:
            return False
        self.repo.delete(obj)
        return True
