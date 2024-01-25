from dataclasses import dataclass

from sqlalchemy import Select, Insert, select, insert

from src.adapters.database.repositories.base_repository import SABaseRepository
from src.adapters.database.models.user import User

from src.application.auth.entities import AuthUserDTO
from src.application.user.interfaces import IUserRepository
from src.application.helpers import hash_password


@dataclass
class UserRepository(SABaseRepository, IUserRepository):

    async def create_user(self, user: AuthUserDTO) -> User:
        query: Insert = (
            insert(
                User
            )
            .values(
                username=user.username,
                password=hash_password(user.password)
            )
            .returning(
                User
            )
        )
        user = self.session.execute(query).scalar_one()
        self.session.commit()
        return user
    
    async def get_user_by_username(self, username: str) -> User:
        query: Select = (
            select(
                User.id,
                User.username,
                User.password,
            )
            .filter(
                User.username == username
            )
        )
        user = self.session.execute(query).fetchone()
        return user
    
    async def get_user_by_id(self, user_id: int) -> User:
        query: Select = (
            select(
                User.id,
                User.username,
            )
            .filter(
                User.id == user_id
            )
        )
        user = self.session.execute(query).fetchone()
        return user
