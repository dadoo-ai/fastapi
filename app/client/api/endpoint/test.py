import json

from fastapi import APIRouter, Response


router = APIRouter()


@router.get("/")
async def say_hello():

    return Response(
        content=json.dumps(
            {"message": "hello world"}
        ),
        media_type="application/json",
        status_code=200,
    )


@router.get("/enjoy")
async def say_hello_enjoy():

    return Response(
        content=json.dumps(
            {"message": " hello world !!!!!!"}
        ),
        media_type="application/json",
        status_code=200,
    )
