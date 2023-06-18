from functools import lru_cache

from pydantic import BaseSettings


class Config(BaseSettings):
    ...


@lru_cache
def get_config():
    return Config()
