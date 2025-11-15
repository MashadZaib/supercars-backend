from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.hs_code import HsCode


class HsCodeRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, obj: HsCode) -> HsCode:
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def list(self) -> List[HsCode]:
        return self.db.query(HsCode).order_by(HsCode.id.desc()).all()

    def get(self, hs_code_id: int) -> Optional[HsCode]:
        return self.db.query(HsCode).filter(HsCode.id == hs_code_id).first()

    def get_by_code(self, code: str) -> Optional[HsCode]:
        return self.db.query(HsCode).filter(HsCode.code == code).first()

    def update(self, db_obj: HsCode, **changes) -> HsCode:
        for k, v in changes.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete(self, db_obj: HsCode) -> None:
        self.db.delete(db_obj)
        self.db.commit()
