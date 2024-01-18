from app.models.user import User
from app.repositories.user_repository import UserRepository
from http.client import HTTPException


class UserServices:
    def __init__(self, user_repo: UserRepository):
        self.repo = user_repo

    async def create_user(self, user: User):
        new_user = await self.repo.create_user(user)
        if not new_user:
            raise HTTPException(status_code=401, detail="User is already exist")
        return new_user

    async def get_user_by_email(self, email: str):
        return await self.repo.get_user_by_email(email)

    async def check_exist_user(self, email: str, password: str):
        user = await self.repo.check_by_email_and_password(email=email, password=password)
        if not user:
            return False
        return True
