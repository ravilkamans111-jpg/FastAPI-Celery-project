from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import User

class RepoUser:
    async def get_all_users(session: AsyncSession):
        stmt = select(User).order_by(User.id)
        result: Result = await session.execute(stmt)
        users = result.scalars().all()
        return list(users)

user_repos = RepoUser()