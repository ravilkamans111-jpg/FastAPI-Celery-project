import asyncio
from http.client import HTTPException

from pydantic import EmailStr

from api_v1.tasks.reposetory import repo_task
from repos_users import user_repos
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import select

from core.models import db_help, User
from users.shemas import UserCreate

''' Сервисы для пользователей '''


class UserService:

    async def create_user(self, session: AsyncSession, user_in: UserCreate):
        new_user = await self.get_user_by_email(session, user_in.email)

        if new_user:
            raise HTTPException(400, 'User in DB')

        user = User(**user_in.model_dump())
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user


    async def get_all_users(self, session: AsyncSession):
        return await user_repos.get_all_users(session)


    async def get_user_by_id(self, session: AsyncSession, user_id: int) -> User | None:
        return await session.get(User, user_id)


    async def get_user_by_email(self, session: AsyncSession, user_email: EmailStr):
        result = await session.execute(select(User).where(User.email==user_email))

        return result.scalar_one_or_none()

user_service = UserService()
