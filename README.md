# Super Cars Backend (FastAPI + SQLAlchemy + PostgreSQL)

A layered architecture backend for the Super Cars invoicing system.

## Structure
- **API layer:** `app/api/v1`
- **Service layer:** `app/services`
- **Repository layer:** `app/repositories`
- **DB model layer:** `app/models`
- **Schemas (Pydantic):** `app/schemas`
- **Core (config/db/deps):** `app/core`

## Getting Started

### 1) Create & activate virtualenv
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate
```

### 2) Install deps
```bash
pip install -r requirements.txt
```

### 3) Configure environment
Copy `.env.example` to `.env` and update `DATABASE_URL`:
```
DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/supercars
```

### 4) Run migrations (Alembic)
```bash
alembic upgrade head
```

### 5) Start server
```bash
uvicorn app.main:app --reload
```

Open: http://127.0.0.1:8000/docs

## Alembic Notes
- Autogenerate migrations when you change models:
```bash
alembic revision --autogenerate -m "init"
alembic upgrade head
```
