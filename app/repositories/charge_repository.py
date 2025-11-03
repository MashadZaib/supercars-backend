from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.charge import Charge

class ChargeRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, obj: Charge) -> Charge:
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def list(self) -> List[Charge]:
        return self.db.query(Charge).order_by(Charge.id.desc()).all()

    def get(self, charge_id: int) -> Optional[Charge]:
        return self.db.query(Charge).filter(Charge.id == charge_id).first()

    def update(self, db_obj: Charge, **changes) -> Charge:
        for k, v in changes.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete(self, db_obj: Charge) -> None:
        self.db.delete(db_obj)
        self.db.commit()
