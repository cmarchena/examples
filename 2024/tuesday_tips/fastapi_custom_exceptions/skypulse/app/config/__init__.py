from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "sqlite+aiosqlite:///./app/database/skypulse.db"
    test: bool = False
    project_name: str = "SkyPulse"


settings = Settings()  # type: ignore