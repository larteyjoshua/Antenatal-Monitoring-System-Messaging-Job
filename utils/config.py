import os
from functools import lru_cache
from typing import Optional
from pydantic import BaseSettings, AnyHttpUrl, validator
import secrets
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Settings(BaseSettings):
    API_KEY: str = os.environ.get("API_KEY")
    API_V1_STR: str = "/api/v1"
    EXPIRY_TIME: int =  os.environ.get("EXPIRY_TIME")
    OTP_LENGTH: int = os.environ.get("OTP_LENGTH")
    TYPE: str = os.environ.get("TYPE")
    MEDIUM: str =  os.environ.get("MEDIUM")
    SEND_SMS_URL:str =  os.environ.get("SEND_SMS_URL")
    MESSAGE_SENDER: str =  os.environ.get("MESSAGE_SENDER")
   
    SQLALCHEMY_DATABASE_URL: str = os.environ.get("DATABASE_URL")
    if SQLALCHEMY_DATABASE_URL and SQLALCHEMY_DATABASE_URL.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URL.replace("postgres://", "postgresql://", 1)
    
  
    class Config:
        case_sensitive = True
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()