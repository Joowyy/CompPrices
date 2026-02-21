from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./prices.db"
    DEBUG: bool = True

settings = Settings()