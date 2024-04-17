import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.client.api.router import routeur


app = FastAPI()

app.include_router(routeur)

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",  # origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    max_age=300,
)


if __name__ == "__main__":
    uvicorn.run("api:app", host='0.0.0.0', port=8000, reload=True, debug=True)
