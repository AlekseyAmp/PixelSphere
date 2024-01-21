from dataclasses import dataclass
from typing import Sequence

from sqlalchemy import Select, Row, Insert, select, insert

from adapters.database.repositories.base_repository import SABaseRepository
from adapters.database.models.user import User

from application.user.entities import UserDTO
from application.user.interfaces import IUserRepository
from application.user.helpers import hash_password


@dataclass
class UserRepository(SABaseRepository, IUserRepository):
    async def create_user(self, user: UserDTO) -> User:
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
                User
            )
            .filter(
                User.username == username
            )
        )
        user = self.session.execute(query).scalar_one()
        return user