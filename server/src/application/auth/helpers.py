from datetime import timedelta

from adapters.api.settings import settings, AuthJWT


def create_access_token(authorize: AuthJWT, user_id: str) -> str:
    access_token = authorize.create_access_token(
        subject=user_id,
        expires_time=timedelta(minutes=int(settings.ACCESS_TOKEN_EXPIRES_IN)),
    )
    return access_token

def create_refresh_token(authorize: AuthJWT, user_id: str) -> str:
    refresh_token = authorize.create_refresh_token(
        subject=user_id,
        expires_time=timedelta(minutes=int(settings.REFRESH_TOKEN_EXPIRES_IN)),
    )
    return refresh_token