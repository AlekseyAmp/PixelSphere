from fastapi import HTTPException
from dataclasses import dataclass


@dataclass
class PhotoNotFound(HTTPException):
    photo_id: int

    def __post_init__(self):
        detail = f"Photo with ID {self.photo_id} not found"
        super().__init__(status_code=404, detail=detail)