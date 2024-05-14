from fastapi import APIRouter

from app.client.api.endpoint import mongo, home


routeur = APIRouter()
routeur.include_router(
    mongo.router, prefix="/test", tags=["test"]
)
routeur.include_router(
    home.router
)
