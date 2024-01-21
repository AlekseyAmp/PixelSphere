from fastapi import Depends
from sqlalchemy.orm import Session

from adapters.database.sa_session import get_session
from adapters.database.repositories.user_repository import (
    UserRepository
)

from application.user.exceptions import UserExists


def get_user_repo(session: Session = Depends(get_session)) -> UserRepository:
    return UserRepository(session)
    
async def check_user_exsist(
    username: str,
    user_repo: UserRepository = Depends(get_user_repo)
) -> None:
    user = await user_repo.get_user_by_username(username)

    if user:
        raise UserExists(username)
    
    return None

