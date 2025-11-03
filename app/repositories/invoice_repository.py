from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.invoice_preview import InvoicePreview

class InvoiceRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, obj: InvoicePreview) -> InvoicePreview:
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def get(self, invoice_id: int) -> Optional[InvoicePreview]:
        return self.db.query(InvoicePreview).filter(InvoicePreview.id == invoice_id).first()

    def list(self) -> List[InvoicePreview]:
        return self.db.query(InvoicePreview).order_by(InvoicePreview.id.desc()).all()

    def update(self, db_obj: InvoicePreview, **changes) -> InvoicePreview:
        for k, v in changes.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete(self, db_obj: InvoicePreview) -> None:
        self.db.delete(db_obj)
        self.db.commit()
