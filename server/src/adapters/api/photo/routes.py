import tempfile

from fastapi import APIRouter, Depends, File, UploadFile
from fastapi.responses import FileResponse

from src.adapters.api.photo.dependencies import get_photo_service, check_exsist_photo
from src.adapters.api.user.dependencies import get_user_id
from src.adapters.api.photo.schemas import (
    AddCommentResponse,
    AddLikeResponse,
    CommentResponse,
    UploadPhotoResponse,
    PhotoResponse
)

from src.application.photo.services import PhotoService
from src.application.photo.entities import PhotoDTO, CommentDTO


router = APIRouter()


@router.post(
    path="/upload_photo",
    response_model=UploadPhotoResponse
)
async def upload_photo(
    title: str,
    description: str,
    file: UploadFile = File(...),
    user_id: int = Depends(get_user_id),
    photo_service: PhotoService = Depends(get_photo_service)
) -> UploadPhotoResponse:
    contents = await file.read()
    photo = PhotoDTO(
        title=title,
        description=description,
        image=contents
    )
    return await photo_service.upload_photo(photo, user_id)

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
    response_model=list[PhotoResponse],
)
async def get_all_photos(
    photo_service: PhotoService = Depends(get_photo_service)
) -> list[PhotoResponse]:
    return await photo_service.get_all_photos()

@router.get(
    path="/get_my_photos",
    response_model=list[PhotoResponse],
)
async def get_my_photos(
    user_id: int = Depends(get_user_id),
    photo_service: PhotoService = Depends(get_photo_service)
) -> list[PhotoResponse]:
    return await photo_service.get_my_photos(user_id)

@router.get(
    path="/search_photos",
    response_model=list[PhotoResponse],
)
async def search_photos(
    search_term: str,
    photo_service: PhotoService = Depends(get_photo_service)
) -> list[PhotoResponse]:
    return await photo_service.search_photos(search_term)

@router.get(
    path="/download_photo/{photo_id}",
)
async def download_photo(
    photo_id: int = Depends(check_exsist_photo),
    photo_service: PhotoService = Depends(get_photo_service)
) -> FileResponse:
    binary_data = await photo_service.download_photo(photo_id)

    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(binary_data)
    
    return FileResponse(temp_file.name, filename=f"{temp_file.name}.jpg")

@router.delete(
    path="/delete_photo/{photo_id}",
    response_model=dict[str, str],
)
async def delete_photo(
    photo_id: int = Depends(check_exsist_photo),
    user_id: int = Depends(get_user_id),
    photo_service: PhotoService = Depends(get_photo_service)
) -> dict[str, str]:
    return await photo_service.delete_photo(photo_id, user_id)

@router.post(
    path="/add_comment_to_photo",
    response_model=AddCommentResponse,
)
async def add_comment_to_photo(
    comment: CommentDTO,
    photo_id: int = Depends(check_exsist_photo),
    user_id: int = Depends(get_user_id),
    photo_service: PhotoService = Depends(get_photo_service)
) -> AddCommentResponse:
    return await photo_service.add_comment_to_photo(photo_id, comment, user_id)

@router.get(
    path="/get_comments_for_photo/{photo_id}",
    response_model=list[CommentResponse],
)
async def get_comments_for_photo(
    photo_id: int = Depends(check_exsist_photo),
    photo_service: PhotoService = Depends(get_photo_service)
) -> list[CommentResponse]:
    return await photo_service.get_comments_for_photo(photo_id)

@router.post(
    path="/add_like_to_photo",
    response_model=AddLikeResponse,
)
async def add_like_to_photo(
    photo_id: int = Depends(check_exsist_photo),
    user_id: int = Depends(get_user_id),
    photo_service: PhotoService = Depends(get_photo_service)
) -> AddLikeResponse:
    return await photo_service.add_like_to_photo(photo_id, user_id)

@router.get(
    path="/get_likes_for_photo/{photo_id}",
    response_model=dict[str, int],
)
async def get_likes_for_photo(
    photo_id: int = Depends(check_exsist_photo),
    photo_service: PhotoService = Depends(get_photo_service)
) -> dict[str, int]:
    return await photo_service.get_likes_for_photo(photo_id)
