from typing import Annotated
from users.shemas import UserRead
from users.crud import user_service
from fastapi import APIRouter
from fastapi.params import Depends
from users.shemas import UserCreate
from users.dependencies import user_by_id, SessionDep

user_router = APIRouter(prefix="/users", tags=["Users"])


""" Роуты для пользователей """


@user_router.post("/", response_model=UserRead)
async def create_user(
    user_in: UserCreate, session: SessionDep,
):
    return await user_service.create_user(session=session, user_in=user_in)


@user_router.get("/{user_id}", response_model=UserRead)
async def get_user(user: Annotated[UserRead, Depends(user_by_id)]):
    return user
