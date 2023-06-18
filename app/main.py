from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.routers import users


@asynccontextmanager
async def lifecycle(_app):
    print("API Startup ... ")
    yield
    print("API Cleanup ...")


app = FastAPI(lifespan=lifecycle)

app.include_router(users.router)


@app.get("/")
def index():
    return {"Hello": "User"}
