from typing import Annotated
from fastapi import Depends

from api_v1.tasks.depends import task_by_id
from core.models import Tasks

TaskDep = Annotated[Tasks, Depends(task_by_id)]
