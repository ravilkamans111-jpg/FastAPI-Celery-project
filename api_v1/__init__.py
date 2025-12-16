from fastapi import APIRouter
from .tasks.views import task_router as tasks_router


router = APIRouter()
router.include_router(router=tasks_router, prefix="/Tasks")
