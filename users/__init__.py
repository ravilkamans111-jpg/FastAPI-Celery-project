from fastapi import APIRouter
from users.views import user_router as user_router

router_v2 = APIRouter()

router_v2.include_router(router=user_router)
