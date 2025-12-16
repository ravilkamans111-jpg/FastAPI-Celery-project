from datetime import datetime
from core.models.task import StatusEnum
from pydantic import BaseModel, ConfigDict, Field


class TasksBase(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: str | None
    status: StatusEnum
    created_at: datetime
    updated_at: datetime
    user_id : int


class Task(TasksBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class TaskCreate(TasksBase):
    pass


class TaskUpdate(TasksBase):
    pass


class TaskUpdatePart(BaseModel):
    status: StatusEnum