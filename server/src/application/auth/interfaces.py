from abc import ABC, abstractmethod

from adapters.database.models.user import User

from application.auth.entities import AuthUserDTO


class IAuthRepository(ABC):
    @abstractmethod
    async def create_user(self, user: AuthUserDTO) -> User:
        pass

    @abstractmethod
    async def login_user(self, user: AuthUserDTO) -> tuple:
        pass