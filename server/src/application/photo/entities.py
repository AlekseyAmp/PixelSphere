from pydantic import BaseModel


class PhotoDTO(BaseModel):
    title: str
    description: str
    image: bytes


class CommentDTO(BaseModel):
    text: str
