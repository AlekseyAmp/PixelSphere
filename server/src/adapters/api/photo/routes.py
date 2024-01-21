from fastapi import APIRouter, Depends, File, UploadFile

from adapters.api.photo.dependencies import get_photo_service, check_exsist_photo
from adapters.api.photo.schemas import (
    AddCommentResponse,
    AddLikeResponse,
    CommentResponse,
    UploadPhotoResponse,
    PhotoResponse
)

from application.photo.services import PhotoService
from application.photo.entities import PhotoDTO, CommentDTO


router = APIRouter()


@router.post(
    path="/upload_photo",
    response_model=UploadPhotoResponse
)
async def upload_photo(
    title: str,
    description: str,
    file: UploadFile = File(...),
    photo_service: PhotoService = Depends(get_photo_service),
) -> UploadPhotoResponse:
    contents = await file.read()
    photo = PhotoDTO(
        title=title,
        description=description,
        image=contents
    )
    return await photo_service.upload_photo(photo)


@router.get(
    path="/get_photo/{photo_id}",
    response_model=PhotoResponse,
)
async def get_photo_by_id(
    photo_id: int = Depends(check_exsist_photo),
    photo_service: PhotoService = Depends(get_photo_service)
) -> PhotoResponse:
    return await photo_service.get_photo_by_id(photo_id)


@router.get(
    path="/get_all_photos",
    response_model=dict[str, list[PhotoResponse]],
)
async def get_all_photos(
    photo_service: PhotoService = Depends(get_photo_service)
) -> dict[str, list[PhotoResponse]]:
    return await photo_service.get_all_photos()


@router.post(
    path="/add_comment_to_photo",
    response_model=AddCommentResponse,
)
async def add_comment_to_photo(
    comment: CommentDTO,
    photo_service: PhotoService = Depends(get_photo_service),
    photo_id: int = Depends(check_exsist_photo),
) -> AddCommentResponse:
    return await photo_service.add_comment_to_photo(photo_id, comment)


@router.get(
    path="/get_comments_for_photo/{photo_id}",
    response_model=dict[str, list[CommentResponse]],
)
async def get_comments_for_photo(
    photo_id: int = Depends(check_exsist_photo),
    photo_service: PhotoService = Depends(get_photo_service)
) -> dict[str, list[CommentResponse]]:
    return await photo_service.get_comments_for_photo(photo_id)


@router.post(
    path="/add_like_to_photo",
    response_model=AddLikeResponse,
)
async def add_like_to_photo(
    photo_service: PhotoService = Depends(get_photo_service),
    photo_id: int = Depends(check_exsist_photo),
) -> AddLikeResponse:
    return await photo_service.add_like_to_photo(photo_id)


@router.get(
    path="/get_likes_for_photo/{photo_id}",
    response_model=dict[str, int],
)
async def get_likes_for_photo(
    photo_id: int = Depends(check_exsist_photo),
    photo_service: PhotoService = Depends(get_photo_service)
) -> dict[str, int]:
    return await photo_service.get_likes_for_photo(photo_id)