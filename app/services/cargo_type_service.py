from fastapi import HTTPException, status
from app.repositories.cargo_type_repository import CargoTypeRepository
from app.schemas.cargo_type_schema import CargoTypeCreate

class CargoTypeService:
    def __init__(self, db):
        self.repo = CargoTypeRepository(db)

    def create_cargo_type(self, payload: CargoTypeCreate):
        existing = self.repo.get_by_name(payload.name)
        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Booking Party already exists"
            )
        return self.repo.create(payload.dict())

    def get_booking_parties(self, search: str = None):
        return self.repo.get_all(search)
