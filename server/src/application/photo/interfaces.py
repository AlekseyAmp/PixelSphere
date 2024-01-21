from abc import ABC, abstractmethod
from typing import Sequence

from sqlalchemy import Row

from adapters.database.models.photo import Photo
from adapters.database.models.comment import Comment
from adapters.database.models.like import Like

from application.photo.entities import PhotoDTO, CommentDTO


class IPhotoRepository(ABC):
    @abstractmethod
    async def upload_photo(self, photo: PhotoDTO, user_id: str) -> Photo:
        pass

    @abstractmethod
    async def get_photo_by_id(self, photo_id: int) -> Row | None:
        pass

    @abstractmethod
    async def get_all_photos(self) -> Sequence[Row]:
        pass


class IPhotoCommentRepository(ABC):
    @abstractmethod
    async def add_comment_to_photo(self, photo_id: int, comment: CommentDTO, user_id: str) -> Comment:
        pass

    @abstractmethod
    async def get_comments_for_photo(self, photo_id: int) -> list[tuple]:
        pass


class IPhotoLikeRepository(ABC):
    @abstractmethod
    async def add_like_to_photo(self, photo_id: int, user_id: str) -> Like:
        pass

    @abstractmethod
    async def get_likes_for_photo(self, photo_id: int) -> int:
        pass
