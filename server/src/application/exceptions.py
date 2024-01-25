from fastapi import HTTPException
from dataclasses import dataclass


@dataclass
class PhotoNotFoundException(HTTPException):
    photo_id: int

    def __post_init__(self) -> None:
        detail = f"Photo with ID {self.photo_id} not found"
        super().__init__(status_code=404, detail=detail)


@dataclass
class InvalidFormatException(HTTPException):
    ALLOWED_IMAGE_FORMATS: set

    def __post_init__(self) -> None:
        detail = f"Invalid image format. Allowed formats: {', '.join(self.ALLOWED_IMAGE_FORMATS)}"
        super().__init__(status_code=409, detail=detail)


@dataclass
class CannotRemovePhotoException(HTTPException):
    def __post_init__(self) -> None:
        detail = "You do not have permission to remove this photo."
        super().__init__(status_code=403, detail=detail)


@dataclass
class AlreadyLikedException(HTTPException):
    def __post_init__(self) -> None:
        detail = "You have already liked this photo."
        super().__init__(status_code=403, detail=detail)


@dataclass
class UserExistsException(HTTPException):
    username: str

    def __post_init__(self) -> None:
        detail = f"User with username '{self.username}' already exists"
        super().__init__(status_code=409, detail=detail)


@dataclass
class UserNotFoundException(HTTPException):
    def __post_init__(self) -> None:
        detail = f"User not found"
        super().__init__(status_code=404, detail=detail)
