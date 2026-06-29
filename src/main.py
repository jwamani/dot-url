from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn

from src.container import ApplicationContainer
from src.presentation.api.v1 import link


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    container = ApplicationContainer()
    app.state.container = container
    container.wire(modules=[link])
    yield
    engine = container.engine()
    await engine.dispose()


app = FastAPI(lifespan=lifespan)

app.include_router(link.router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("src.main:app", host="localhost", port=8000, reload=True)
