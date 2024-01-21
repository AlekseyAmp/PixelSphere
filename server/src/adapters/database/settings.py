import os
from dotenv import load_dotenv

from pydantic_settings import BaseSettings


load_dotenv()


class Settings(BaseSettings):
    POSTGRESQL_HOST: str = os.environ["POSTGRESQL_HOST"]
    POSTGRESQL_USER: str = os.environ["POSTGRESQL_USER"]
    POSTGRESQL_PASSWORD: str = os.environ["POSTGRESQL_PASSWORD"]
    POSTGRESQL_DB: str = os.environ["POSTGRESQL_DB"]

    SQLALCHEMY_DB_URL: str = (
        "postgresql+psycopg2://"
        f"{POSTGRESQL_USER}:"
        f"{POSTGRESQL_PASSWORD}@"
        f"{POSTGRESQL_HOST}/"
        f"{POSTGRESQL_DB}"
    )

    TIMEZONE: str = "Asia/Yekaterinburg"


settings = Settings()
