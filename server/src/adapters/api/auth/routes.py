from fastapi import APIRouter, Depends, Response

from adapters.api.auth.dependencies import get_auth_service
from adapters.api.user.dependencies import check_user_exsist
from adapters.api.user.schemas import UserResponse
from adapters.api.settings import AuthJWT

from application.auth.services import AuthService
from application.user.entities import UserDTO


router = APIRouter()


@router.post(
    path="/register_user",
    response_model=UserResponse
)
async def register_user(
    user: UserDTO,
    response: Response,
    authorize: AuthJWT = Depends(),
    # user_exsist = Depends(check_user_exsist),
    auth_service: AuthService = Depends(get_auth_service),
) -> UserResponse:
    return await auth_service.register_user(user, response, authorize)

