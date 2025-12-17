from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Tasks
from core.models.db_helper import db_help
from .crud import task_service
from .depends import task_by_id
from .schemas import TaskCreate, TaskSchema, TaskUpdate, TaskUpdatePart


task_router = APIRouter(tags=["Tasks"])


""" Роутеры для задач"""


@task_router.get(
    "/",
    response_model=list[TaskSchema],
)
async def get_tasks(
    session: AsyncSession = Depends(db_help.session_dependency),
):
    return await task_service.get_tasks(session=session)


@task_router.post(
    "/",
    response_model=TaskSchema,
)
async def create_task(
    task_in: TaskCreate,
    session: AsyncSession = Depends(db_help.session_dependency),
):
    return await task_service.create_task(session=session, task_in=task_in)


@task_router.get(
    "/{task_id}/",
    response_model=TaskSchema,
)
async def get_task(
    task: TaskSchema = Depends(task_by_id),
):
    return task


@task_router.put(
    "/{task_id}/",
)
async def update_task(
    task_update: TaskUpdate,
    task: Tasks = Depends(task_by_id),
    session: AsyncSession = Depends(db_help.session_dependency),
):
    return await task_service.update_task(
        session=session,
        task=task,
        task_update_part=task_update,
    )


@task_router.patch(
    "/tasks/{task_id}/status/",
    response_model=TaskSchema,
)
async def update_task_part(
    task_update: TaskUpdatePart,
    task: Tasks = Depends(task_by_id),
    session: AsyncSession = Depends(db_help.session_dependency),
):
    return await task_service.update_task_part(
        session=session, task=task, task_update_part=task_update, partial=True
    )


@task_router.get(
    "/user/{user_id}",
    response_model=list[TaskSchema],
)
async def get_tasks_by_user(
    user_id: int,
    session: AsyncSession = Depends(db_help.session_dependency),
):
    return await task_service.get_tasks_by_user_id(session=session, user_id=user_id)
