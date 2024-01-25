from fastapi import APIRouter, Depends

from src.adapters.api.user.dependencies import get_user_id, get_user_service
from src.adapters.api.user.schemas import UserResponse

from src.application.user.services import UserService


router = APIRouter()


@router.get(
    path="/get_user",
    response_model=UserResponse,
)
async def get_user_by_id(
    user_id: int = Depends(get_user_id),
    user_service: UserService = Depends(get_user_service)
) -> UserResponse:
    return await user_service.get_user_by_id(user_id)
