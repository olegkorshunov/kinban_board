from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    SECRET_KEY_jwt: str
    ALGORITHM: str

    @property
    def PG_DSN(self) -> PostgresDsn:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    class Config:
        env_file = ".env"


CONFIG = Config()  # type: ignore
