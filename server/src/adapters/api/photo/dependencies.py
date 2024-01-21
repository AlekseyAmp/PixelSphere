from fastapi import Depends
from sqlalchemy.orm import Session

from adapters.database.sa_session import get_session
from adapters.database.repositories.photo_repository import (
    PhotoRepository,
    PhotoCommentRepository,
    PhotoLikeRepository
)
from application.photo.services import PhotoService
from application.photo.exceptions import PhotoNotFound


def get_photo_repo(session: Session = Depends(get_session)) -> PhotoRepository:
    return PhotoRepository(session)

def get_photo_comment_repo(session: Session = Depends(get_session)) -> PhotoCommentRepository:
    return PhotoCommentRepository(session)

def get_photo_like_repo(session: Session = Depends(get_session)) -> PhotoLikeRepository:
    return PhotoLikeRepository(session)

def get_photo_service(
    photo_repo: PhotoRepository = Depends(get_photo_repo),
    comment_repo: PhotoCommentRepository = Depends(get_photo_comment_repo),
    like_repo: PhotoLikeRepository = Depends(get_photo_like_repo)
) -> PhotoService:
    return PhotoService(
        photo_repo,
        comment_repo,
        like_repo
    )
    
async def check_exsist_photo(
    photo_id: int,
    photo_repo: PhotoRepository = Depends(get_photo_repo)
) -> int:
    photo = await photo_repo.get_photo_by_id(photo_id)

    if not photo:
        raise PhotoNotFound(photo_id)
    
    return photo_id

