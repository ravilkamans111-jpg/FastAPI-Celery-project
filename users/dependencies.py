from fastapi import Depends, HTTPException, Path
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from core.models.db_helper import db_help
from users.crud import user_service


""" Зависимости """


async def user_by_id(
    user_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_help.session_dependency),
):
    user = await user_service.get_user_by_id(session=session, user_id=user_id)
    if user is not None:
        return user
    raise HTTPException(status_code=404, detail="Not found")
