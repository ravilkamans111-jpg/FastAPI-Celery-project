from fastapi import Depends, HTTPException, Path
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from api_v1.tasks.crud import task_service
from core.models.db_helper import db_help



async def task_by_id(task_id: Annotated[int, Path],
                     session: AsyncSession = Depends(db_help.session_dependency)):
    task = await task_service.get_task(session=session, task_id=task_id)
    if task is not None:
        return task
    raise HTTPException(status_code=404, detail='Not found')


