from typing import Annotated

import config
from fastapi import Depends, Security

Config = Annotated[config.Config, Depends(config.get_config)]


def Scopes(*scopes):
    return Security(scopes=scopes)
