from fastapi import FastAPI
from app.core.config import settings
from app.core.database import Base, engine
from app.api.v1 import invoices, booking_requests, booking_confirmations, clients_info


# Create tables if not using Alembic yet (safe when starting out)
# Comment out in production and use Alembic migrations instead.
# Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.APP_NAME)

# Routers
app.include_router(invoices.router, prefix="/api/v1/invoices", tags=["invoices"])

app.include_router(booking_requests.router, prefix="/api/v1/booking-requests", tags=["Booking Requests"])
app.include_router(
    booking_confirmations.router,
    prefix="/api/v1/booking-confirmations",
    tags=["Booking Confirmations"]
)

app.include_router(
    clients_info.router,
    prefix="/api/v1/client-info",
    tags=["Client Info"]
)
@app.get("/health")
def health():
    return {"status": "ok"}
