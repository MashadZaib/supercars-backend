from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.shipping_instruction import ShippingInstruction
from app.repositories.shipping_instruction_repository import ShippingInstructionRepository
from app.schemas.shipping_instruction_schema import ShippingInstructionCreate, ShippingInstructionUpdate

class ShippingInstructionService:
    def __init__(self, db: Session):
        self.repo = ShippingInstructionRepository(db)

    def create_instruction(self, payload: ShippingInstructionCreate) -> ShippingInstruction:
        obj = ShippingInstruction(**payload.dict())
        return self.repo.create(obj)

    def list_instructions(self) -> List[ShippingInstruction]:
        return self.repo.list()

    def get_instruction(self, instruction_id: int) -> Optional[ShippingInstruction]:
        return self.repo.get(instruction_id)

    def update_instruction(self, instruction_id: int, payload: ShippingInstructionUpdate) -> Optional[ShippingInstruction]:
        obj = self.repo.get(instruction_id)
        if not obj:
            return None
        return self.repo.update(obj, **payload.dict(exclude_unset=True))

    def delete_instruction(self, instruction_id: int) -> bool:
        obj = self.repo.get(instruction_id)
        if not obj:
            return False
        self.repo.delete(obj)
        return True
