from dataclasses import dataclass

from src.application.exceptions import UserNotFoundException
from src.application.user.interfaces import IUserRepository


@dataclass
class UserService:
    user_repo: IUserRepository

    async def get_user_by_id(self, user_id: int) -> dict:
        user = await self.user_repo.get_user_by_id(user_id)

        if not user:
            raise UserNotFoundException()

        return {
            "id": user.id,
            "username": user.username
        }
