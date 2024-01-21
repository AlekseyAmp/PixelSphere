from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from adapters.api.photo import routes


app = FastAPI(title="PixelSphere", version="0.1")


origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes.router, tags=['item'], prefix='/api')


@app.get("/")
def root():
    return {"message": "Go to /docs"}