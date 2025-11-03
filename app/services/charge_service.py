from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.charge import Charge
from app.repositories.charge_repository import ChargeRepository
from app.schemas.charge_schema import ChargeCreate, ChargeUpdate

class ChargeService:
    def __init__(self, db: Session):
        self.repo = ChargeRepository(db)

    def create_charge(self, payload: ChargeCreate) -> Charge:
        obj = Charge(**payload.dict())
        return self.repo.create(obj)

    def list_charges(self) -> List[Charge]:
        return self.repo.list()

    def get_charge(self, charge_id: int) -> Optional[Charge]:
        return self.repo.get(charge_id)

    def update_charge(self, charge_id: int, payload: ChargeUpdate) -> Optional[Charge]:
        obj = self.repo.get(charge_id)
        if not obj:
            return None
        return self.repo.update(obj, **payload.dict(exclude_unset=True))

    def delete_charge(self, charge_id: int) -> bool:
        obj = self.repo.get(charge_id)
        if not obj:
            return False
        self.repo.delete(obj)
        return True
