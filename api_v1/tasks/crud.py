from core.tasks import process_task
from .reposetory import repo_task
from sqlalchemy.ext.asyncio import AsyncSession
from core.models.task import Tasks
from api_v1.tasks.schemas import TaskCreate, TaskUpdate, TaskUpdatePart

"""Сервисы для создания, просмотра и тд"""


class TaskService:
    async def get_tasks(self, session: AsyncSession) -> list[Tasks]:
        return await repo_task.get_all_tasks(session)

    async def get_task(self, session: AsyncSession, task_id: int) -> Tasks | None:
        return await session.get(Tasks, task_id)

    async def create_task(self, session: AsyncSession, task_in: TaskCreate):
        task = Tasks(**task_in.model_dump())
        session.add(task)
        await session.commit()
        await session.refresh(task)
        process_task.delay(task.id)

        return task

    async def update_task(
        self,
        session: AsyncSession,
        task: Tasks,
        task_update_part: TaskUpdate,
        partial=False,
    ):
        for key, value in task_update_part.model_dump(exclude_unset=partial).items():
            setattr(task, key, value)
        await session.commit()
        return task

    async def update_task_part(
        self,
        session: AsyncSession,
        task: Tasks,
        task_update_part: TaskUpdatePart,
        partial=False,
    ):
        for key, value in task_update_part.model_dump(exclude_unset=partial).items():
            setattr(task, key, value)
        await session.commit()
        return task

    async def delete_task(self, session: AsyncSession, task: Tasks):
        await session.delete(task)
        await session.commit()

    async def get_tasks_by_user_id(self, session: AsyncSession, user_id: int):
        return await repo_task.get_tasks_by_users_if(session, user_id)


task_service = TaskService()
