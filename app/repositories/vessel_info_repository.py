from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.vessel_info import VesselInfo


class VesselInfoRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, obj: VesselInfo) -> VesselInfo:
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def list(self) -> List[VesselInfo]:
        return self.db.query(VesselInfo).order_by(VesselInfo.id.desc()).all()

    def get(self, vessel_id: int) -> Optional[VesselInfo]:
        return self.db.query(VesselInfo).filter(VesselInfo.id == vessel_id).first()

    def update(self, db_obj: VesselInfo, **changes) -> VesselInfo:
        for k, v in changes.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete(self, db_obj: VesselInfo) -> None:
        self.db.delete(db_obj)
        self.db.commit()
