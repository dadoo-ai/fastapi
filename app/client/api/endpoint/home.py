import json

from fastapi import APIRouter, Response


router = APIRouter()


@router.get("/")
async def root():

    return Response(
        content=json.dumps(
            {"message": "bienvenue"}
        ),
        media_type="application/json",
        status_code=200,
    )
