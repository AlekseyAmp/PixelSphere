from dataclasses import dataclass

from fastapi import Response, HTTPException

from adapters.api.user.schemas import UserResponse
from adapters.api.settings import settings, AuthJWT

from application.user.entities import UserDTO
from application.user.interfaces import IUserRepository
from application.auth.helpers import create_access_token, create_refresh_token


@dataclass
class AuthService:
    user_repo: IUserRepository

    async def register_user(self, user: UserDTO, response: Response, authorize: AuthJWT) -> dict[str, UserResponse] | None:
        try:
            user_data = await self.user_repo.create_user(user)
            if user_data:
                access_token = create_access_token(authorize, str(user_data.id))
                refresh_token = create_refresh_token(authorize, str(user_data.id))

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
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Internal Server Error: {str(e)}"
            )       
        
        

    def login_user(self, user: UserDTO, response: Response, authorize):
        pass
        # user = db.query(User).filter(
        #     User.phone_number == data.phone_number
        # ).first()

        # if not user:
        #     raise HTTPException(
        #         status_code=404,
        #         detail="User not found"
        #     )

        # if not verify_password(data.password, user.password):
        #     raise HTTPException(
        #         status_code=400,
        #         detail="Wrong phone number or password"
        #     )

        # access_token = create_access_token(authorize, str(user.id))
        # refresh_token = create_refresh_token(authorize, str(user.id))

        # response.set_cookie("access_token",
        #                     access_token,
        #                     settings.ACCESS_TOKEN_EXPIRES_IN * 60,
        #                     settings.ACCESS_TOKEN_EXPIRES_IN * 60,
        #                     "/",
        #                     None,
        #                     False,
        #                     True,
        #                     "lax"
        #                     )

        # response.set_cookie("refresh_token",
        #                     refresh_token,
        #                     settings.REFRESH_TOKEN_EXPIRES_IN * 60,
        #                     settings.REFRESH_TOKEN_EXPIRES_IN * 60,
        #                     "/",
        #                     None,
        #                     False,
        #                     True,
        #                     "lax"
        #                     )

        # return {
        #     "id": user.id,
        #     "name": user.name,
        #     "surname": user.surname,
        #     "phone_number": user.phone_number,
        #     "email": user.email,
        #     "role": user.role,
        #     "access_token": access_token,
        #     "refresh_token": refresh_token
        # }

    def refresh_token(response: Response, authorize, user_id: str):
        access_token = create_access_token(authorize, user_id)

        response.set_cookie("access_token",
                            access_token,
                            settings.ACCESS_TOKEN_EXPIRES_IN * 60,
                            settings.ACCESS_TOKEN_EXPIRES_IN * 60,
                            "/",
                            None,
                            False,
                            True,
                            "lax")

        return { 
            "access_token": access_token
        }

    def logout_user(response: Response, authorize):
        authorize.unset_jwt_cookies()
        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")
        return {
            "message": "You're logout"
        }
