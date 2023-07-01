from fastapi import APIRouter

from example_api.deps import Scopes

router = APIRouter()


@router.get("/users/", tags=["users"], dependencies=[Scopes("get:user")])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/users/me", tags=["users"], dependencies=[Scopes("get:user")])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/users/{username}", tags=["users"], dependencies=[Scopes("get:user")])
async def read_user(username: str):
    return {"username": username}
