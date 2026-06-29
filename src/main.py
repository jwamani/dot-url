from fastapi import FastAPI
import uvicorn


from src.presentation.api.v1 import link

app = FastAPI()

app.include_router(link.router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="localhost",
        port=8000
    )