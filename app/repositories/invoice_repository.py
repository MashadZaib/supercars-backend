from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.invoice import Invoice

class InvoiceRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, obj: Invoice) -> Invoice:
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def get(self, invoice_id: int) -> Optional[Invoice]:
        return self.db.query(Invoice).filter(Invoice.id == invoice_id).first()

    def list(self) -> List[Invoice]:
        return self.db.query(Invoice).order_by(Invoice.id.desc()).all()

    def update(self, db_obj: Invoice, **changes) -> Invoice:
        for k, v in changes.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete(self, db_obj: Invoice) -> None:
        self.db.delete(db_obj)
        self.db.commit()
