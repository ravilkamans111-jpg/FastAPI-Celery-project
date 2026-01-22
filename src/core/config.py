from pathlib import Path
from pydantic_settings import BaseSettings


BASE_DIR = Path(__file__).parent.parent


class Setting(BaseSettings):
    api_v1_prefix: str = "/api/1"
    db_url: str = f"sqlite+aiosqlite:///{BASE_DIR}/test.db"
    echo: bool = True


settings = Setting()
