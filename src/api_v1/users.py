from typing import Annotated
from src.schemas.users import UserRead
from src.crud.users import user_service
from fastapi import APIRouter
from fastapi.params import Depends
from src.schemas.users import UserCreate
from src.deps.dependencies import user_by_id, SessionDep

user_router = APIRouter(prefix="/users", tags=["Users"])


""" Роуты для пользователей """


from fastapi import APIRouter
from src.api_v1.users import user_router as user_router

router_v2 = APIRouter()

router_v2.include_router(router=user_router)


@user_router.get('/', response_model=list[UserRead])
async def get_all_users(
        session: SessionDep,
):
    return await user_service.get_all_users(session)

@user_router.post("/", response_model=UserRead)
async def create_user(
    user_in: UserCreate, session: SessionDep,
):
    return await user_service.create_user(session=session, user_in=user_in)


@user_router.get("/{user_id}", response_model=UserRead)
async def get_user(user: Annotated[UserRead, Depends(user_by_id)]):
    return user
