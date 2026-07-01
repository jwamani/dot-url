from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn
import logging

from src.container import Container
from src.presentation.api.v1 import link
from src.infrastructure.database.base import Base
from src.config.logging_conf import setup_logging

setup_logging()

logger = logging.getLogger(__name__)


container = Container()
engine = container.engine()


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)



@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    await init_models()
    logger.info("Application startup: Database models initialized.")
    yield
    logger.info("Shutting down: Closing database connection...")
    await engine.dispose()


app = FastAPI(lifespan=lifespan)

app.include_router(link.router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("src.main:app", host="localhost", port=8000, reload=True)
