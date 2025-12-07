import os
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="CloudGuru Backend",
    version="1.0.0",
    description="Simple Python backend for the CloudGuru home task"
)


class Item(BaseModel):
    id: int
    name: str
    price: float


ITEMS = [
    Item(id=1, name="First item", price=10.5),
    Item(id=2, name="Second item", price=20.0),
]


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "cloudguru-backend",
        "environment": os.getenv("APP_ENV", "local"),
    }


@app.get("/api/v1/items", response_model=List[Item])
def list_items():
    return ITEMS


@app.get("/api/v1/secret")
def get_secret():
    secret_value = os.getenv("APP_SECRET", "not-set")
    return {"secret": secret_value}
