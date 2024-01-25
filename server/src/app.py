from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.adapters.api.auth import routes as AuthRouter
from src.adapters.api.user import routes as UserRouter
from src.adapters.api.photo import routes as PhotoRouter


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

app.include_router(AuthRouter.router, tags=['auth'], prefix='/api')
app.include_router(UserRouter.router, tags=['user'], prefix='/api')
app.include_router(PhotoRouter.router, tags=['photo'], prefix='/api')


@app.get("/")
def root():
    return {"message": "Go to /docs"}
