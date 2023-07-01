from functools import lru_cache
from typing import Annotated

import fastapi_auth0.auth as fastapi_auth0
from fastapi import Depends, Security

from example_api.config import Config as _Config
from example_api.config import get_config


@lru_cache
def get_verifier():
    config = get_config()
    return fastapi_auth0.Auth0(
        domain=config.AUTH0_DOMAIN,
        api_audience=config.AUTH0_API_AUDIENCE,
        scopes={"some": "scope"},
    )


TokenUser = Annotated[fastapi_auth0.Auth0User, Depends(get_verifier().get_user)]

Config = Annotated[_Config, Depends(get_config)]


def Scopes(*scopes):
    return Security(get_verifier().get_user, scopes=scopes)
