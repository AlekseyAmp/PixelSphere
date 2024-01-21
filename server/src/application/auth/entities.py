from pydantic import BaseModel


class AuthUserDTO(BaseModel):
    username: str
    password: str
