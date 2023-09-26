import os
from functools import lru_cache
from pydantic_settings import BaseSettings
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Settings(BaseSettings):
    API_KEY: str = os.environ.get("API_KEY")
    MEDIUM: str = os.environ.get("MEDIUM")
    SEND_SMS_URL: str = os.environ.get("SEND_SMS_URL")
    SENDER_ID: str = os.environ.get("SENDER_ID")
    SEND_VOICE_SMS_URL: str = os.environ.get("SEND_VOICE_SMS_URL")
    SQLALCHEMY_DATABASE_URL: str = os.environ.get("DATABASE_URL")
    MNOTIFY_VOICE_SMS_URL: str = os.environ.get("MNOTIFY_VOICE_SMS_URL")
    MNOTIFY_API_KEY: str = os.environ.get("MNOTIFY_API_KEY")
    if SQLALCHEMY_DATABASE_URL and SQLALCHEMY_DATABASE_URL.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URL.replace(
            "postgres://", "postgresql://", 1)

    class Config:
        case_sensitive = True
        env_file = ".env"
        extra = "allow"


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
