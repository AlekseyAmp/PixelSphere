from fastapi import Depends, HTTPException, Request
from sqlalchemy.orm import Session

from adapters.database.sa_session import get_session
from adapters.database.repositories.user_repository import (
    UserRepository
)

from application.auth.services import AuthService


def get_user_repo(session: Session = Depends(get_session)) -> UserRepository:
    return UserRepository(session)

def get_auth_service(
    user_repo: UserRepository = Depends(get_user_repo),
) -> AuthService:
    return AuthService(
        user_repo
    )

def check_user_authenticated(request: Request)-> bool:
    credentials_exception = HTTPException(
        status_code=401,
        detail="You are already authenticated",
    )

    access_token = request.cookies.get("access_token")
    refresh_token = request.cookies.get("refresh_token")

    if access_token or refresh_token:
        raise credentials_exception

    return True
