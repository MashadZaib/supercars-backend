from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.carrier_info import CarrierInfo
from app.repositories.carrier_info_repository import CarrierInfoRepository
from app.schemas.carrier_info_schema import CarrierInfoCreate, CarrierInfoUpdate


class CarrierInfoService:
    def __init__(self, db: Session):
        self.repo = CarrierInfoRepository(db)

    def create_carrier(self, payload: CarrierInfoCreate) -> CarrierInfo:
        obj = CarrierInfo(**payload.dict())
        return self.repo.create(obj)

    def list_carriers(self) -> List[CarrierInfo]:
        return self.repo.list()

    def get_carrier(self, carrier_id: int) -> Optional[CarrierInfo]:
        return self.repo.get(carrier_id)

    def update_carrier(self, carrier_id: int, payload: CarrierInfoUpdate) -> Optional[CarrierInfo]:
        obj = self.repo.get(carrier_id)
        if not obj:
            return None
        return self.repo.update(obj, **payload.dict(exclude_unset=True))

    def delete_carrier(self, carrier_id: int) -> bool:
        obj = self.repo.get(carrier_id)
        if not obj:
            return False
        self.repo.delete(obj)
        return True
