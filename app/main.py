import os

from fastapi import FastAPI

app = FastAPI(title="AI CI/CD Failure Investigator Lab")

APP_NAME = os.getenv("APP_NAME", "AI CI/CD Failure Investigator")


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "AI CI/CD Failure Investigator Lab", "app": APP_NAME}


@app.get("/index")
def index() -> dict[str, str]:
    """Alias for root endpoint."""
    return {"message": "AI CI/CD Failure Investigator Lab", "app": APP_NAME}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "app": APP_NAME}
