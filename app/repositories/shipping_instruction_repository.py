from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.shipping_instruction import ShippingInstruction

class ShippingInstructionRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, obj: ShippingInstruction) -> ShippingInstruction:
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def list(self) -> List[ShippingInstruction]:
        return self.db.query(ShippingInstruction).order_by(ShippingInstruction.id.desc()).all()

    def get(self, instruction_id: int) -> Optional[ShippingInstruction]:
        return self.db.query(ShippingInstruction).filter(ShippingInstruction.id == instruction_id).first()

    def update(self, db_obj: ShippingInstruction, **changes) -> ShippingInstruction:
        for k, v in changes.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete(self, db_obj: ShippingInstruction) -> None:
        self.db.delete(db_obj)
        self.db.commit()
