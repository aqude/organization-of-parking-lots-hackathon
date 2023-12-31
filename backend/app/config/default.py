from os import environ
from decimal import Decimal
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from pydantic import BaseSettings
from cryptography.fernet import Fernet


class DefaultSettings(BaseSettings):
    """
    Default configs for application.

    Usually, we have three environments: for development, testing and production.
    But in this situation, we only have standard settings for local development.
    """

    ENV: str = environ.get("ENV", "local")
    PATH_PREFIX: str = environ.get("PATH_PREFIX", "/api/v1")
    APP_HOST: str = environ.get("APP_HOST", "http://127.0.0.1")
    APP_PORT: int = int(environ.get("APP_PORT", 8000))

    POSTGRES_DB: str = environ.get("POSTGRES_DB", "db")
    POSTGRES_HOST: str = environ.get("POSTGRES_HOST", "localhost")  # for local fast api service
    #POSTGRES_HOST: str = environ.get("POSTGRES_HOST", "db")  # for docker-compose
    POSTGRES_USER: str = environ.get("POSTGRES_USER", "user")
    POSTGRES_PORT: int = int(environ.get("POSTGRES_PORT", "5432")[-4:])
    POSTGRES_PASSWORD: str = environ.get("POSTGRES_PASSWORD", "hackme")
    DB_CONNECT_RETRY: int = environ.get("DB_CONNECT_RETRY", 20)
    DB_POOL_SIZE: int = environ.get("DB_POOL_SIZE", 15)

    # to get a string like this run: "openssl rand -hex 32"
    SECRET_KEY: str = environ.get("SECRET_KEY", "")
    ALGORITHM: str = environ.get("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(environ.get("ACCESS_TOKEN_EXPIRE_MINUTES", 1440))

    SERVICE_NAME: str = environ.get("SERVICE_NAME", "")
    PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")
    OAUTH2_SCHEME = OAuth2PasswordBearer(tokenUrl=f"/api/v1/user/authentication")

    One_Gradus = Decimal(63046.689652997775)
    EART_RADIUS = Decimal(6371210)

    LOG_FILE: str = environ.get("LOG_FILE", "operations.log")

    CELERY_BROKER_URL: str = environ.get(
        "CELERY_BROKER_URL", "redis://127.0.0.1:6379/0"
    )
    CELERY_RESULT_BACKEND: str = environ.get(
        "CELERY_BROKER_URL", "redis://127.0.0.1:6379/0"
    )

    YOOKASSA_ACCOUNT_ID: str = environ.get("YOOKASSA_ACCOUNT_ID", "")
    YOOKASSA_SECRET_KEY: str = environ.get("YOOKASSA_SECRET_KEY", "")

    LOG_SECRET_KEY = Fernet.generate_key()

    @property
    def enctyption(self) -> Fernet:
        return Fernet(self.LOG_SECRET_KEY)

    @property
    def database_settings(self) -> dict:
        """
        Get all settings for connection with database.
        """
        return {
            "database": self.POSTGRES_DB,
            "user": self.POSTGRES_USER,
            "password": self.POSTGRES_PASSWORD,
            "host": self.POSTGRES_HOST,
            "port": self.POSTGRES_PORT,
        }

    @property
    def database_uri(self) -> str:
        """
        Get uri for connection with database.
        """
        return "postgresql+asyncpg://{user}:{password}@{host}:{port}/{database}".format(
            **self.database_settings,
        )

    @property
    def database_uri_sync(self) -> str:
        """
        Get uri for connection with database.
        """
        return "postgresql://{user}:{password}@{host}:{port}/{database}".format(
            **self.database_settings,
        )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
