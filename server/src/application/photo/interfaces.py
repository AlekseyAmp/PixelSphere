from abc import ABC, abstractmethod
from typing import Sequence

from sqlalchemy import Row

from src.adapters.database.models.photo import Photo
from src.adapters.database.models.comment import Comment
from src.adapters.database.models.like import Like

from src.application.photo.entities import PhotoDTO, CommentDTO


class IPhotoRepository(ABC):

    @abstractmethod
    async def upload_photo(self, photo: PhotoDTO, user_id: int) -> Photo:
        pass

    @abstractmethod
    async def get_photo_by_id(self, photo_id: int) -> Row | None:
        pass

    @abstractmethod
    async def get_all_photos(self) -> Sequence[Row]:
        pass

    @abstractmethod
    async def get_my_photos(self, user_id: int) -> Sequence[Row]:
        pass

    @abstractmethod
    async def search_photos(self, search_term: str) -> Sequence[Row]:
        pass

    @abstractmethod
    async def delete_photo(self, photo_id: int, user_id: int) -> int:
        pass


class IPhotoCommentRepository(ABC):

    @abstractmethod
    async def add_comment_to_photo(self, photo_id: int, comment: CommentDTO, user_id: int) -> Comment:
        pass

    @abstractmethod
    async def get_comments_for_photo(self, photo_id: int) -> list[tuple]:
        pass


class IPhotoLikeRepository(ABC):

    @abstractmethod
    async def add_like_to_photo(self, photo_id: int, user_id: int) -> Like:
        pass

    @abstractmethod
    async def get_likes_for_photo(self, photo_id: int) -> int:
        pass

    @abstractmethod
    async def get_like_by_user_and_photo_id(self, photo_id: int, user_id: int) -> Like:
        pass
