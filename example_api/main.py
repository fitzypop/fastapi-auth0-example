from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI

from example_api.deps import get_verifier
from example_api.routers import users


@asynccontextmanager
async def lifecycle(_app):
    print("API Startup ... ")
    yield
    print("API Cleanup ...")


app = FastAPI(
    lifespan=lifecycle, dependencies=[Depends(get_verifier().implicit_scheme)]
)

app.include_router(users.router)


@app.get("/")
def index():
    return {"Hello": "User"}
