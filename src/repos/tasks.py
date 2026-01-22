from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.task import Tasks
from src.schemas.tasks import TaskUpdatePart

"""Работа с базой данных в crud"""


class RepoTask:
    async def get_all_tasks(self, session: AsyncSession) -> list[Tasks]:
        stmt = select(Tasks).order_by(Tasks.id)
        result: Result = await session.execute(stmt)
        return list(result.scalars().all())

    async def get_tasks_by_users_if(self, session: AsyncSession, user_id: int):
        stmt = select(Tasks).where(Tasks.user_id == user_id).order_by(Tasks.id)
        result = await session.execute(stmt)
        return list(result.scalars().all())

    async def update_task_func(
            session: AsyncSession, task: Tasks, task_update: TaskUpdatePart, partial=False
    ):
        for key, value in task_update.model_dump(exclude_unset=partial).items():
            setattr(task, key, value)
        await session.commit()
        return task


repo_task = RepoTask()
