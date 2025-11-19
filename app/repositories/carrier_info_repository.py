from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.carrier_info import CarrierInfo


class CarrierInfoRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, obj: CarrierInfo) -> CarrierInfo:
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def list(self) -> List[CarrierInfo]:
        return self.db.query(CarrierInfo).order_by(CarrierInfo.id.desc()).all()

    def get(self, carrier_id: int) -> Optional[CarrierInfo]:
        return self.db.query(CarrierInfo).filter(CarrierInfo.id == carrier_id).first()

    def update(self, db_obj: CarrierInfo, **changes) -> CarrierInfo:
        for k, v in changes.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete(self, db_obj: CarrierInfo) -> None:
        self.db.delete(db_obj)
        self.db.commit()
