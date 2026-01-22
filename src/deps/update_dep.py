from typing import Annotated
from fastapi import Depends

from src.deps.depends import task_by_id
from src.models import Tasks

TaskDep = Annotated[Tasks, Depends(task_by_id)]
