from enum import Enum
from typing import Literal, Optional

from pydantic import BaseModel, BaseSettings, PostgresDsn


class DatabasePool(BaseModel):
    MIN_SIZE: Optional[int] = None  # noqa: WPS115
    MAX_SIZE: Optional[int] = None  # noqa: WPS115


class Config(BaseSettings):
    DATABASE_URL: PostgresDsn = PostgresDsn("postgresql://postgres@localhost/tsm")  # noqa: WPS115

    class Env(str, Enum):  # noqa: WPS600
        PRODUCTION = "production"  # noqa: WPS115
        DEVELOPMENT = "development"  # noqa: WPS115

    ENV: Env = Env.DEVELOPMENT  # noqa: WPS115

    LOG_LEVEL: Literal["FATAL", "ERROR", "WARN", "INFO", "DEBUG"] = "DEBUG"  # noqa: WPS115


config = Config()
