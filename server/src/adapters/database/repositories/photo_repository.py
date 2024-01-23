from dataclasses import dataclass
from typing import Sequence

from sqlalchemy import Select, Row, Insert, func, select, insert

from adapters.database.repositories.base_repository import SABaseRepository
from adapters.database.models.user import User
from adapters.database.models.photo import Photo
from adapters.database.models.comment import Comment
from adapters.database.models.like import Like

from application.photo.entities import PhotoDTO, CommentDTO
from application.photo.interfaces import (
    IPhotoRepository,
    IPhotoCommentRepository,
    IPhotoLikeRepository
)


@dataclass
class PhotoRepository(SABaseRepository, IPhotoRepository):
    async def upload_photo(self, photo: PhotoDTO, user_id: int) -> Photo:
        query: Insert = (
            insert(
                Photo
            )
            .values(
                title=photo.title,
                description=photo.description,
                image=photo.image,
                user_id=user_id
            )
            .returning(
                Photo
            )
        )
        photo = self.session.execute(query).scalar_one()
        self.session.commit()
        return photo

    async def get_photo_by_id(self, photo_id: int) -> Row | None:
        query: Select = (
            select(
                Photo.title,
                Photo.description,
                Photo.image,
                Photo.created_at,
                User.username
            )
            .join(
                User,
                Photo.user_id == User.id
            )
            .filter(
                Photo.id == photo_id
            )
        )
        photo = self.session.execute(query).fetchone()
        return photo

    async def get_all_photos(self) -> Sequence[Row]:
        query: Select = (
            select(
                Photo.id,
                Photo.title,
                Photo.description,
                Photo.image,
                Photo.created_at,
                User.username
            )
            .join(
                User,
                Photo.user_id == User.id
            )
        )
        photos = self.session.execute(query).fetchall()
        return photos


@dataclass
class PhotoCommentRepository(SABaseRepository, IPhotoCommentRepository):
    async def add_comment_to_photo(self, photo_id: int, comment: CommentDTO, user_id: int) -> Comment:
        query: Insert = (
            insert(
                Comment
            )
            .values(
                text=comment.text,
                photo_id=photo_id,
                user_id=user_id,
            )
            .returning(
                Comment
            )
        )
        comment = self.session.execute(query).scalar_one()
        self.session.commit()
        return comment

    async def get_comments_for_photo(self, photo_id: int) -> list[tuple]:
        query: Select = (
            select(
                Comment.id,
                Comment.text,
                Comment.created_at,
                User.username,
            )
            .join(
                User,
                Comment.user_id == User.id
            )
            .filter(
                Comment.photo_id == photo_id
            )
        )
        comments = self.session.execute(query).fetchall()
        return comments


@dataclass
class PhotoLikeRepository(SABaseRepository, IPhotoLikeRepository):
    async def add_like_to_photo(self, photo_id: int, user_id: int) -> Like:
        query: Insert = (
            insert(
                Like
            )
            .values(
                user_id=user_id,
                photo_id=photo_id
            )
            .returning(
                Like
            )
        )
        like = self.session.execute(query).scalar_one()
        self.session.commit()
        return like

    async def get_likes_for_photo(self, photo_id: int) -> int:
        query: Select = (
            select(
                func.sum(1).label("total_likes")
            )
            .filter(
                Like.photo_id == photo_id
            )
        )
        total_likes = self.session.execute(query).scalar_one()
        return total_likes if total_likes is not None else 0
