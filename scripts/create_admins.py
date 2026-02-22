"""Create several admin users in the database for testing.

Run:

    python scripts/create_admins.py

This script will:
- create tables if they don't exist
- create a dummy test user: username **test** / password **test** (for quick testing)
- create 5 admin users (username admin1...admin5) with password 'Password123!'
- skip any user that already exists

Note: Change the PASSWORD constant to a secure value in real deployments.
"""
import os
from app.database import engine, SessionLocal, Base
from app import models
from app import crud

# ensure tables exist
Base.metadata.create_all(bind=engine)

# Dummy user for quick testing (username: test, password: test)
DUMMY_TEST_USER = ("test", "test@example.com")
DUMMY_TEST_PASSWORD = "test"

ADMINS = [
    ("admin1", "admin1@example.com"),
    ("admin2", "admin2@example.com"),
    ("admin3", "admin3@example.com"),
    ("admin4", "admin4@example.com"),
    ("admin5", "admin5@example.com"),
]

PASSWORD = os.environ.get('CARIZO_ADMIN_PASSWORD', 'Password123!')


def main():
    db = SessionLocal()
    created = 0
    try:
        # Create dummy test user (test / test)
        username, email = DUMMY_TEST_USER
        existing = db.query(models.User).filter((models.User.username == username) | (models.User.email == email)).first()
        if not existing:
            user_in = type('U', (), {'username': username, 'email': email, 'password': DUMMY_TEST_PASSWORD})
            user = crud.create_user(db, user_in)
            user.is_superuser = True
            db.add(user)
            db.commit()
            print(f"Created dummy test user: {username} / {email} (password: {DUMMY_TEST_PASSWORD})")
            created += 1
        else:
            print(f"Skipping existing user: {username} / {email}")

        for username, email in ADMINS:
            existing = db.query(models.User).filter((models.User.username == username) | (models.User.email == email)).first()
            if existing:
                print(f"Skipping existing user: {username} / {email}")
                continue
            # use CRUD helpers to create (which hashes password)
            user_in = type('U', (), {'username': username, 'email': email, 'password': PASSWORD})
            user = crud.create_user(db, user_in)
            # set superuser flag
            user.is_superuser = True
            db.add(user)
            db.commit()
            print(f"Created admin: {username} / {email}")
            created += 1
    finally:
        db.close()

    print(f"Done. {created} user(s) created.")
    print("Dummy login for testing: username=test, password=test")
    print(f"Admin logins: admin1..admin5, password={PASSWORD}")

if __name__ == '__main__':
    main()
