from fastapi import APIRouter
from src.api_v1.tasks_router import task_router as tasks_router


router = APIRouter()
router.include_router(router=tasks_router, prefix="/Tasks")
