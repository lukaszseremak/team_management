from enum import Enum
from typing import Literal, Optional

from pydantic import BaseModel, BaseSettings, PostgresDsn


class DatabasePool(BaseModel):
    MIN_SIZE: Optional[int] = None
    MAX_SIZE: Optional[int] = None


class Config(BaseSettings):
    DATABASE_URL: PostgresDsn = "postgresql://postgres@localhost/tsm"

    class Env(str, Enum):
        PRODUCTION = "production"
        DEVELOPMENT = "development"

    ENV: Env = Env.DEVELOPMENT

    LOG_LEVEL: Literal["FATAL", "ERROR", "WARN", "INFO", "DEBUG"] = "DEBUG"


config = Config()
