from abc import ABC, abstractmethod

from adapters.database.models.user import User

from application.user.entities import UserDTO


class IUserRepository(ABC):
    @abstractmethod
    async def create_user(self, user: UserDTO) -> User:
        pass

    @abstractmethod
    async def get_user_by_username(self, username: str) -> User:
        pass