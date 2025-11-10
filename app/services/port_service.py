from fastapi import HTTPException, status
from app.repositories.port_repository import PortRepository
from app.schemas.port_schema import PortCreate

class PortService:
    def __init__(self, db):
        self.repo = PortRepository(db)

    def create_port(self, payload: PortCreate):
        existing = self.repo.get_by_name(payload.name)
        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Booking Party already exists"
            )
        return self.repo.create(payload.dict())

    def get_ports(self, search: str = None):
        return self.repo.get_all(search)
