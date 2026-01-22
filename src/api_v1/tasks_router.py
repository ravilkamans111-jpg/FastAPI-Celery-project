from fastapi import APIRouter

from src.crud.tasks import task_service
from src.deps.depends import SessionDep
from src.schemas.tasks import TaskCreate, TaskSchema, TaskUpdate, TaskUpdatePart
from src.deps.update_dep import TaskDep

task_router = APIRouter(tags=["Tasks"])


""" Роутеры для задач"""


@task_router.get(
    "/",
    response_model=list[TaskSchema],
)
async def get_tasks(
    session: SessionDep,
):
    return await task_service.get_tasks(session=session)


@task_router.post(
    "/",
    response_model=TaskSchema,
)
async def create_task(
    task_in: TaskCreate,
    session: SessionDep,
):
    return await task_service.create_task(session=session, task_in=task_in)


@task_router.get(
    "/{task_id}/",
    response_model=TaskSchema,
)
async def get_task(
    task: TaskDep,
):
    return task


@task_router.put(
    "/{task_id}/",
)
async def update_task(
    task_update: TaskUpdate,
    task: TaskDep,
    session: SessionDep,
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
    task: TaskDep,
    session: SessionDep,
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
    session: SessionDep,
):
    return await task_service.get_tasks_by_user_id(session=session, user_id=user_id)
