from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.invoice_preview import InvoicePreview
from app.repositories.invoice_preview_repository import InvoicePreviewRepository
from app.schemas.invoice_preview_schema import InvoicePreviewCreate, InvoicePreviewUpdate

class InvoicePreviewService:
    def __init__(self, db: Session):
        self.repo = InvoicePreviewRepository(db)

    def create_preview(self, payload: InvoicePreviewCreate) -> InvoicePreview:
        obj = InvoicePreview(**payload.dict())
        return self.repo.create(obj)

    def list_previews(self) -> List[InvoicePreview]:
        return self.repo.list()

    def get_preview(self, preview_id: int) -> Optional[InvoicePreview]:
        return self.repo.get(preview_id)

    def update_preview(self, preview_id: int, payload: InvoicePreviewUpdate) -> Optional[InvoicePreview]:
        obj = self.repo.get(preview_id)
        if not obj:
            return None
        return self.repo.update(obj, **payload.dict(exclude_unset=True))

    def delete_preview(self, preview_id: int) -> bool:
        obj = self.repo.get(preview_id)
        if not obj:
            return False
        self.repo.delete(obj)
        return True
