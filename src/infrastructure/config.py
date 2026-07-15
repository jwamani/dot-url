from pydantic_settings import BaseSettings
from typing import Literal

class Settings(BaseSettings):
    db_url: str
    redis_url: str = "redis://localhost:6379/0"
    environment: Literal["development", "production"]  = "development"

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}