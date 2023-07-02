from functools import lru_cache
from typing import Annotated

import fastapi_auth0.auth as fastapi_auth0
from fastapi import Depends, Security

from example_api.config import ApiConfig as _APiConfig
from example_api.config import api_config


@lru_cache
def verifier():
    config = api_config()
    return fastapi_auth0.Auth0(
        domain=config.AUTH0_DOMAIN,
        api_audience=config.AUTH0_API_AUDIENCE,
        scopes={"some": "scope"},
    )


TokenUser = Annotated[fastapi_auth0.Auth0User, Depends(verifier().get_user)]

APIConfig = Annotated[_APiConfig, Depends(api_config)]


def Scopes(*scopes):
    return Security(verifier().get_user, scopes=scopes)
