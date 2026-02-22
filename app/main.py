from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from . import models, schemas, crud, auth
from .database import engine, get_db, Base
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from sqlalchemy.orm import Session

# create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title='Carizo Backend')

# Allow the frontend dev server to call the API during development.
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/api/auth/signup', response_model=schemas.UserOut)
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = crud.get_user_by_username(db, user.username) or crud.get_user_by_email(db, user.email)
    if existing:
        raise HTTPException(status_code=400, detail='User with that username or email already exists')
    created = crud.create_user(db, user)
    return created

@app.post('/api/auth/token', response_model=schemas.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect username or password', headers={'WWW-Authenticate': 'Bearer'})
    access_token = auth.create_access_token(data={'sub': user.username})
    return {'access_token': access_token, 'token_type': 'bearer'}

@app.get('/api/users/me', response_model=schemas.UserOut)
async def read_users_me(current_user: models.User = Depends(auth.get_current_user)):
    return current_user


@app.post('/api/bookings', response_model=schemas.BookingOut)
def create_booking(booking: schemas.BookingCreate, db: Session = Depends(get_db), current_user: models.User = Depends(auth.get_current_user)):
    return crud.create_booking(db, booking)


@app.get('/api/bookings', response_model=List[schemas.BookingOut])
def list_bookings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: models.User = Depends(auth.get_current_user)):
    return crud.get_bookings(db, skip, limit)


@app.get('/api/bookings/{booking_id}', response_model=schemas.BookingOut)
def get_booking(booking_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(auth.get_current_user)):
    b = crud.get_booking(db, booking_id)
    if not b:
        raise HTTPException(status_code=404, detail='Booking not found')
    return b
