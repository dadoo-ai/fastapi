from fastapi import APIRouter

from app.client.api.endpoint import test


routeur = APIRouter()
routeur.include_router(
    test.router, prefix="/test", tags=["test"]
)
