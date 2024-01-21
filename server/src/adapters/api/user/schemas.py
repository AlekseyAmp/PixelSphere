from datetime import datetime
from pydantic import BaseModel


class UserResponse(BaseModel):
    id: int
    username: str
    created_at: datetime
    access_token: str
    refresh_token: str