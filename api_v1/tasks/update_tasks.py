from sqlalchemy.ext.asyncio import AsyncSession
from core.models.task import Tasks
from api_v1.tasks.schemas import TaskUpdatePart


async def update_task_func(
            session: AsyncSession,
            task: Tasks,
            task_update: TaskUpdatePart,
            partial = False):
    for key, value in task_update.model_dump(exclude_unset=partial).items():
        setattr(task, key, value)
    await session.commit()
    return task