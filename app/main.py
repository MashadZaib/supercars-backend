from fastapi import FastAPI
from app.core.config import settings
from app.core.database import Base, engine
from app.api.v1 import clients, invoices

# Create tables if not using Alembic yet (safe when starting out)
# Comment out in production and use Alembic migrations instead.
# Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.APP_NAME)

# Routers
app.include_router(clients.router, prefix="/api/v1/clients", tags=["clients"])
app.include_router(invoices.router, prefix="/api/v1/invoices", tags=["invoices"])

@app.get("/health")
def health():
    return {"status": "ok"}
