import os
from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:postgres@localhost:5432/supercars")
    APP_NAME: str = os.getenv("APP_NAME", "Super Cars API")
    APP_DEBUG: bool = os.getenv("APP_DEBUG", "true").lower() == "true"

settings = Settings()
