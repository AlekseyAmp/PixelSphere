from abc import ABC, abstractmethod

from application.photo.entities import PhotoDTO, CommentDTO


class IPhotoRepository(ABC):
    @abstractmethod
    async def upload_photo(self, photo: PhotoDTO, user_id: str) -> tuple:
        pass

    @abstractmethod
    async def get_photo_by_id(self, photo_id: int) -> tuple:
        pass

    @abstractmethod
    async def get_all_photos(self) -> list[tuple]:
        pass


class IPhotoCommentRepository(ABC):
    @abstractmethod
    async def add_comment_to_photo(self, photo_id: int, comment: CommentDTO, user_id: str) -> tuple:
        pass

    @abstractmethod
    async def get_comments_for_photo(self, photo_id: int) -> list[tuple]:
        pass


class IPhotoLikeRepository(ABC):
    @abstractmethod
    async def add_like_to_photo(self, photo_id: int, user_id: str) -> tuple:
        pass

    @abstractmethod
    async def get_likes_for_photo(self, photo_id: int) -> tuple:
        pass
