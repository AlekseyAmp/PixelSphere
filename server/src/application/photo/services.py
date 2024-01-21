import base64
from dataclasses import dataclass

from fastapi import HTTPException

from application.photo.entities import PhotoDTO, CommentDTO
from application.photo.interfaces import (
    IPhotoRepository,
    IPhotoCommentRepository,
    IPhotoLikeRepository,
)
from adapters.api.photo.schemas import(
    AddLikeResponse,
    UploadPhotoResponse,
    PhotoResponse,
    AddCommentResponse,
    CommentResponse
)


@dataclass
class PhotoService:
    photo_repo: IPhotoRepository
    comment_repo: IPhotoCommentRepository
    like_repo: IPhotoLikeRepository

    async def upload_photo(self, photo: PhotoDTO, user_id: int = 1) -> UploadPhotoResponse:
        try:
            photo_data = await self.photo_repo.upload_photo(photo, user_id)
            if photo_data:
                return {
                    "id": photo_data.id,
                    "title": photo_data.title,
                    "description": photo_data.description,
                    "created_at": photo_data.created_at
                }
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Internal Server Error: {str(e)}"
            )

    async def get_photo_by_id(self, photo_id: int) -> PhotoResponse:
        photo_data = await self.photo_repo.get_photo_by_id(photo_id)

        image_base64 = base64.b64encode(photo_data.image).decode('utf-8')
        comments = await self.get_comments_for_photo(photo_id)
        likes = await self.get_likes_for_photo(photo_id)
        return {
            "id": photo_id,
            "title": photo_data.title,
            "description": photo_data.description,
            "image": image_base64,
            "created_at": photo_data.created_at,
            "comments": comments["comments"],
            "likes": likes["total_likes"],
            "author": photo_data.username
        }

    async def get_all_photos(self) -> dict[str, list[PhotoResponse]]:
        photos = await self.photo_repo.get_all_photos()

        photos_list = []
        for photo in photos:
            if photo:
                image_base64 = base64.b64encode(photo.image).decode('utf-8')
                comments = await self.get_comments_for_photo(photo.id)
                likes = await self.get_likes_for_photo(photo.id)
                photos_list.append({
                    "id": photo.id,
                    "title": photo.title,
                    "description": photo.description,
                    "image": image_base64,
                    "created_at": photo.created_at,
                    "comments": comments["comments"],
                    "likes": likes["total_likes"],
                    "author": photo.username
                })
        return {"photos": photos_list}

    async def add_comment_to_photo(self, photo_id: int, comment: CommentDTO, user_id: int = 1) -> AddCommentResponse:
        try:
            comment_data = await self.comment_repo.add_comment_to_photo(photo_id, comment, user_id)
            if comment_data:
                return {
                    "id": comment_data.id,
                    "photo_id": comment_data.photo_id,
                    "text": comment_data.text,
                    "created_at": comment_data.created_at
                }
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Internal Server Error: {str(e)}"
            )

    async def get_comments_for_photo(self, photo_id: int) -> dict[str, list[CommentResponse]]:
        comments = await self.comment_repo.get_comments_for_photo(photo_id)            

        comments_list = []
        for comment in comments:
            comments_list.append({
                "id": comment.id,
                "text": comment.text,
                "created_at": comment.created_at,
                "author": comment.username,
            })
        return {"comments": comments_list}

    async def add_like_to_photo(self, photo_id: int, user_id: int = 1) -> AddLikeResponse:
        try:
            like_data = await self.like_repo.add_like_to_photo(photo_id, user_id)
            if like_data:
                return {
                    "id": like_data.id,
                    "photo_id": like_data.photo_id,
                    "created_at": like_data.created_at,
                }
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Internal Server Error: {str(e)}"
            )

    async def get_likes_for_photo(self, photo_id: int) -> dict[str, int]:
        total_likes = await self.like_repo.get_likes_for_photo(photo_id)
        return {
            "total_likes": total_likes
        }
