from fastapi import APIRouter, Depends, Response

from adapters.api.auth.dependencies import (
    get_auth_service,
    check_user_authenticated,
)
from adapters.api.user.dependencies import get_user_id
from adapters.api.auth.schemas import (
    RegisterResponse,
    LoginResponse,
)
from adapters.api.settings import AuthJWT

from application.auth.services import AuthService
from application.auth.entities import AuthUserDTO


router = APIRouter()


@router.post(
    path="/register_user",
    response_model=RegisterResponse,
    dependencies=[Depends(check_user_authenticated)]
)
async def register_user(
    user: AuthUserDTO,
    response: Response,
    authorize: AuthJWT = Depends(),
    auth_service: AuthService = Depends(get_auth_service)
) -> RegisterResponse:
    return await auth_service.register_user(
        user,
        response,
        authorize
    )

@router.post(
    path="/login_user",
    response_model=LoginResponse,
    dependencies=[Depends(check_user_authenticated)],
)
async def login_user(
    user: AuthUserDTO,
    response: Response,
    authorize: AuthJWT = Depends(),
    auth_service: AuthService = Depends(get_auth_service)
) -> LoginResponse:
    return await auth_service.login_user(
        user,
        response,
        authorize
    )

@router.post(
    path="/refresh_token",
    response_model=dict[str, str],
)
async def refresh_token(
    response: Response,
    authorize: AuthJWT = Depends(),
    user_id: int = Depends(get_user_id),
    auth_service: AuthService = Depends(get_auth_service)
) -> dict[str, str]:
    return await auth_service.refresh_token(
        response,
        authorize,
        user_id
    )

@router.post(
    path="/logout_user",
    response_model=dict[str, str],
)
async def logout_user(
    response: Response,
    authorize: AuthJWT = Depends(),
    auth_service: AuthService = Depends(get_auth_service)
) -> dict[str, str]:
    return await auth_service.logout_user(
        response,
        authorize
    )
