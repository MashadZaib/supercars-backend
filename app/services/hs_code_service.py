from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.hs_code import HsCode
from app.repositories.hs_code_repository import HsCodeRepository
from app.schemas.hs_code_schema import HsCodeCreate, HsCodeUpdate


class HsCodeService:
    def __init__(self, db: Session):
        self.repo = HsCodeRepository(db)

    def create_hs_code(self, payload: HsCodeCreate) -> HsCode:
        obj = HsCode(**payload.dict())
        return self.repo.create(obj)

    def list_hs_codes(self) -> List[HsCode]:
        return self.repo.list()

    def get_hs_code(self, hs_code_id: int) -> Optional[HsCode]:
        return self.repo.get(hs_code_id)

    def update_hs_code(self, hs_code_id: int, payload: HsCodeUpdate) -> Optional[HsCode]:
        obj = self.repo.get(hs_code_id)
        if not obj:
            return None
        return self.repo.update(obj, **payload.dict(exclude_unset=True))

    def delete_hs_code(self, hs_code_id: int) -> bool:
        obj = self.repo.get(hs_code_id)
        if not obj:
            return False
        self.repo.delete(obj)
        return True
