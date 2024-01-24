from fastapi_jwt_auth.exceptions import MissingTokenError
from fastapi import Depends, HTTPException

from adapters.api.settings import AuthJWT


def get_user_id(authorize: AuthJWT = Depends()) -> str:
    try:
        authorize.jwt_required()
        user_id = authorize.get_jwt_subject()
        return int(user_id)
    except MissingTokenError:
        raise HTTPException(
            status_code=401,
            detail="Not authorized"
        )
