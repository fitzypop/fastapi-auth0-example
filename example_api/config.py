from functools import lru_cache

from pydantic import BaseSettings


class ApiConfig(BaseSettings):
    AUTH0_API_AUDIENCE: str
    AUTH0_DOMAIN: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache
def api_config():
    return ApiConfig()  # type: ignore
