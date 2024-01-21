from datetime import datetime
from pydantic import BaseModel


class UploadPhotoResponse(BaseModel):
    id: int
    title: str
    description: str
    created_at: datetime


class PhotoResponse(BaseModel):
    id: int
    title: str
    description: str
    image: bytes
    created_at: datetime
    likes: int
    comments: list[dict]
    author: str


class AddCommentResponse(BaseModel):
    id: int
    photo_id: int
    text: str
    created_at: datetime


class CommentResponse(BaseModel):
    id: int
    text: str
    created_at: datetime
    author: str


class AddLikeResponse(BaseModel):
    id: int
    photo_id: int
    created_at: datetime