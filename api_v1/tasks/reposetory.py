from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from core.models.task import Tasks



'''Работа с базой данных в crud'''
class RepoTask:
    async def get_all_tasks(self, session: AsyncSession) -> list[Tasks]:
        stmt = select(Tasks).order_by(Tasks.id)
        result: Result = await session.execute(stmt)
        tasks = result.scalars().all()
        return list(tasks)


    async def get_tasks_by_users_if(self,
            session: AsyncSession,
            user_id: int):
        stmt = select(Tasks).where(Tasks.user_id == user_id)
        result = await session.execute(stmt)
        tasks = result.scalars().all()
        return list(tasks)


repo_task = RepoTask()