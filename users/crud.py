import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_help, User
from users.shemas import UserCreate

''' Сервисы для пользователей '''


class UserService:

    async def create_user(self, session: AsyncSession, user_in: UserCreate):
        user = User(**user_in.model_dump())
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user


    async def get_user_by_id(self, session: AsyncSession, user_id: int) -> User | None:
        return await session.get(User, user_id)


user_service = UserService()
