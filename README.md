# backend-carizo

FastAPI backend for Carizo (auth + users) using PostgreSQL and JWT.

Quick start

1. Create a Python virtualenv and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Set environment variables (example using .env or export):

```bash
export DATABASE_URL=postgresql://postgres:password@localhost:5432/carizo_db
export SECRET_KEY="a-very-secret-key"
export ACCESS_TOKEN_EXPIRE_MINUTES=60
```

3. Run the app:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

4. Create test users (optional, for login testing):

```bash
python scripts/create_admins.py
```

This creates a **dummy test user** (username: **test**, password: **test**) and admin users (admin1..admin5, password: Password123!).

5. Open docs at http://localhost:8000/docs

Notes
- The app will create tables automatically on startup with SQLAlchemy's create_all (use migrations for production).
- This provides basic signup/login/token functionality for JWT-based authentication.
- For production, use a real secret key and HTTPS; do not use create_all in production — use Alembic migrations.
