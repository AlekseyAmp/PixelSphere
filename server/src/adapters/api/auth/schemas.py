from datetime import datetime
from pydantic import BaseModel


class RegisterResponse(BaseModel):
    id: int
    username: str
    created_at: datetime
    access_token: str
    refresh_token: str


class LoginResponse(BaseModel):
    id: int
    username: str
    access_token: str
    refresh_token: str
