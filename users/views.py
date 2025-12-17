from users.shemas import UserRead
from users.crud import user_service
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.models.db_helper import db_help
from users.shemas import UserCreate
from users.dependencies import user_by_id


user_router = APIRouter(prefix='/users', tags= ['Users'])


''' Роуты для пользователей '''

@user_router.post('/', response_model = UserRead)
async def create_user(
    user_in: UserCreate,
    session: AsyncSession = Depends(db_help.session_dependency)
):
    return await user_service.create_user(session=session, user_in=user_in)


@user_router.get('/{user_id}', response_model = UserRead)
async def get_user_by_id(user : UserRead = Depends(user_by_id)):
    return user
