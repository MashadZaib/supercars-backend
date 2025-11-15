from fastapi import FastAPI
from app.core.config import settings
from app.core.database import Base, engine
from app.api.v1 import invoice_previews, booking_requests, booking_confirmations, clients_info, shipping_instructions, charges, booking_parties, cargo_types, ports, users,hs_codes, cargo_descriptions, request_types
from fastapi.middleware.cors import CORSMiddleware


# Create tables if not using Alembic yet (safe when starting out)
# Comment out in production and use Alembic migrations instead.
# Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.APP_NAME)

# Routers

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # Frontend URLs allowed
    allow_credentials=True,
    allow_methods=["*"],            # GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],            # Authorization, Content-Type, etc.
)
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
app.include_router(
    shipping_instructions.router,
    prefix="/api/v1/shipping-instructions",
    tags=["Shipping Instructions"]
)
app.include_router(
    charges.router,
    prefix="/api/v1/charges",
    tags=["Charges"]
)
app.include_router(
    invoice_previews.router,
    prefix="/api/v1/invoice-previews",
    tags=["Invoice Previews"]
)
app.include_router(
    booking_parties.router,
    prefix="/api/v1/booking-parties",
    tags=["Booking Parties"]
)
app.include_router(
    ports.router,
    prefix="/api/v1/ports",
    tags=["Ports"]
)

app.include_router(
    users.router,
    prefix="/api/v1/users",
    tags=["Users"]
)
app.include_router(
    cargo_types.router,
    prefix="/api/v1/cargo-types",
    tags=["Cargo Types"]
)

app.include_router(
    hs_codes.router,
    prefix="/api/v1/hs-codes",
    tags=["HS Codes"]
)

app.include_router(
    cargo_descriptions.router,
    prefix="/api/v1/cargo-descriptions",
    tags=["Cargo Descriptions"]
)
app.include_router(
    request_types.router,
    prefix="/api/v1/request-types",
    tags=["Request Types"]
)

@app.get("/health")
def health():
    return {"status": "ok"}
