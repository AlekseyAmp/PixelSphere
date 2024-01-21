from fastapi import Depends
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