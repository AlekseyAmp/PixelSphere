from datetime import timedelta
from dataclasses import dataclass

from fastapi import Response, HTTPException

from adapters.api.auth.schemas import RegisterResponse, LoginResponse
from adapters.api.settings import settings, AuthJWT

from application.auth.entities import AuthUserDTO
from application.auth.exceptions import UserExistsException, UserNotFoundException
from application.user.interfaces import IUserRepository
from application.helpers import verify_password, validate_non_empty_fields


class TokenService:
    def create_access_token(
        self,
        authorize: AuthJWT,
        user_id: str
    ) -> str:
        access_token = authorize.create_access_token(
            subject=user_id,
            expires_time=timedelta(
                minutes=int(
                    settings.ACCESS_TOKEN_EXPIRES_IN
                )
            ),
        )
        return access_token

    def create_refresh_token(
        self,
        authorize: AuthJWT,
        user_id: str
    ) -> str:
        refresh_token = authorize.create_refresh_token(
            subject=user_id,
            expires_time=timedelta(
                minutes=int(
                    settings.REFRESH_TOKEN_EXPIRES_IN
                )
            ),
        )
        return refresh_token


@dataclass
class AuthService:
    user_repo: IUserRepository

    async def register_user(
        self,
        user: AuthUserDTO,
        response: Response,
        authorize: AuthJWT
    ) -> RegisterResponse:
        validate_non_empty_fields(dict(user))

        user_exsist = await self.user_repo.get_user_by_username(
            user.username
        )

        if user_exsist:
            raise UserExistsException(user.username)

        user_data = await self.user_repo.create_user(user)
        if user_data:
            access_token = TokenService().create_access_token(
                authorize,
                str(user_data.id)
            )
            refresh_token = TokenService().create_refresh_token(
                authorize,
                str(user_data.id)
            )

            response.set_cookie(
                "access_token",
                access_token,
                settings.ACCESS_TOKEN_EXPIRES_IN * 60,
                settings.ACCESS_TOKEN_EXPIRES_IN * 60,
                "/",
                None,
                False,
                True,
                "lax"
            )

            response.set_cookie(
                "refresh_token",
                refresh_token,
                settings.REFRESH_TOKEN_EXPIRES_IN * 60,
                settings.REFRESH_TOKEN_EXPIRES_IN * 60,
                "/",
                None,
                False,
                True,
                "lax"
            )
            
            return {
                "id": user_data.id,
                "username": user_data.username,
                "created_at": user_data.created_at,
                "access_token": access_token,
                "refresh_token": refresh_token
            }    

    async def login_user(
        self,
        user: AuthUserDTO,
        response: Response,
        authorize: AuthJWT
    ) -> LoginResponse:
        validate_non_empty_fields(dict(user))

        user_data = await self.user_repo.get_user_by_username(
            user.username
        )

        if not user_data:
            raise UserNotFoundException(user.username)

        if not verify_password(user.password, user_data.password):
            raise HTTPException(
                status_code=400,
                detail="Wrong username or password"
            )

        access_token = TokenService().create_access_token(
            authorize,
            str(user_data.id)
        )
        refresh_token = TokenService().create_refresh_token(
            authorize,
            str(user_data.id)
        )

        response.set_cookie(
            "access_token",
            access_token,
            settings.ACCESS_TOKEN_EXPIRES_IN * 60,
            settings.ACCESS_TOKEN_EXPIRES_IN * 60,
            "/",
            None,
            False,
            True,
            "lax"
        )

        response.set_cookie(
            "refresh_token",
            refresh_token,
            settings.REFRESH_TOKEN_EXPIRES_IN * 60,
            settings.REFRESH_TOKEN_EXPIRES_IN * 60,
            "/",
            None,
            False,
            True,
            "lax"
        )

        return {
            "id": user_data.id,
            "username": user_data.username,
            "access_token": access_token,
            "refresh_token": refresh_token
        }

    async def refresh_token(
        self,
        response: Response,
        authorize: AuthJWT,
        user_id: int
    ) -> dict[str, str]:
        access_token = TokenService().create_access_token(
            authorize,
            str(user_id)
        )

        response.set_cookie(
            "access_token",
            access_token,
            settings.ACCESS_TOKEN_EXPIRES_IN * 60,
            settings.ACCESS_TOKEN_EXPIRES_IN * 60,
            "/",
            None,
            False,
            True,
            "lax"
        )

        return { 
            "access_token": access_token
        }

    async def logout_user(
        self,
        response: Response,
        authorize: AuthJWT
    ) -> dict[str, str]:
        authorize.unset_jwt_cookies()
        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")
        return {
            "message": "You're logout"
        }
