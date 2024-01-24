from fastapi import HTTPException
from dataclasses import dataclass


@dataclass
class UserExistsException(HTTPException):
    username: str

    def __post_init__(self) -> None:
        detail = f"User with username '{self.username}' already exists"
        super().__init__(status_code=409, detail=detail)


@dataclass
class UserNotFoundException(HTTPException):
    username: str

    def __post_init__(self) -> None:
        detail = f"User with username '{self.username}' not found"
        super().__init__(status_code=404, detail=detail)
