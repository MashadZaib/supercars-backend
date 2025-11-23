from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.vessel_info import VesselInfo
from app.repositories.vessel_info_repository import VesselInfoRepository
from app.schemas.vessel_info_schema import VesselInfoCreate, VesselInfoUpdate


class VesselInfoService:
    def __init__(self, db: Session):
        self.repo = VesselInfoRepository(db)

    def create_vessel(self, payload: VesselInfoCreate) -> VesselInfo:
        obj = VesselInfo(**payload.dict())
        return self.repo.create(obj)

    def list_vessels(self) -> List[VesselInfo]:
        return self.repo.list()

    def get_vessel(self, vessel_id: int) -> Optional[VesselInfo]:
        return self.repo.get(vessel_id)

    def update_vessel(self, vessel_id: int, payload: VesselInfoUpdate) -> Optional[VesselInfo]:
        obj = self.repo.get(vessel_id)
        if not obj:
            return None
        return self.repo.update(obj, **payload.dict(exclude_unset=True))

    def delete_vessel(self, vessel_id: int) -> bool:
        obj = self.repo.get(vessel_id)
        if not obj:
            return False
        self.repo.delete(obj)
        return True
