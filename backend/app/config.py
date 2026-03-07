from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    DATABASE_URL: str
    JWT_SECRET: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    DEFAULT_HOST_USERNAME: str
    DEFAULT_HOST_PASSWORD: str

    REDIS_HOST: str
    REDIS_PORT: int

    class Config:
        env_file = ".env"


settings = Settings()