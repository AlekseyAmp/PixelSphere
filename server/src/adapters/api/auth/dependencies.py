from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from adapters.database.sa_session import get_session
from adapters.database.repositories.user_repository import (
    UserRepository
)
from adapters.api.settings import AuthJWT

from application.auth.services import AuthService


def get_user_repo(session: Session = Depends(get_session)) -> UserRepository:
    return UserRepository(session)

def get_auth_service(
    user_repo: UserRepository = Depends(get_user_repo),
) -> AuthService:
    return AuthService(
        user_repo
    )

def check_user_authenticated(authorize: AuthJWT = Depends()):
    credentials_exception = HTTPException(
        status_code=401,
        detail="You is already authenticated",
    )
    authorize.jwt_required()
    user_id = authorize.get_jwt_subject()
    if user_id:
        raise credentials_exception
    return True
