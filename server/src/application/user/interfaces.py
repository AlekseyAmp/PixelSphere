from abc import ABC, abstractmethod

from src.adapters.database.models.user import User

from src.application.auth.entities import AuthUserDTO


class IUserRepository(ABC):

    @abstractmethod
    async def create_user(self, user: AuthUserDTO) -> User:
        pass

    @abstractmethod
    async def get_user_by_username(self, username: str) -> User:
        pass

    @abstractmethod
    async def get_user_by_id(self, user_id: int) -> User:
        pass
