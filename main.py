from contextlib import asynccontextmanager
from core.config import settings
import uvicorn
from api_v1 import router as router_v1
from fastapi import FastAPI
from users import router_v2


@asynccontextmanager
async def lifespan(app: FastAPI):
    # async with db_help.engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(router=router_v1, prefix=settings.api_v1_prefix)
app.include_router(router=router_v2)



if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
# @app.get('/users/{user_id}/', tags=['Get user by id'])
# async def get_users():
#     ...
#
#
# # @app.post('/tasks/', tags=['Add tasks'])
# # async def add_tasks(task: TaskSchema, session: SessionDep):
# #     new_task = TaskModel(
# #
# #     )
# #     session.add(new_task)
# #     await session.commit()
#
# @app.get('/tasks/{task_id}/', tags=['Get task by id'])
# async def get_tasks():
#     ...
#
#
# @app.get('//tasks/?user_id={ID}', tags=['Get user tasks by id'])
# async def get_user_tasks_by_id():
#     ...
#
#
# @app.patch('/tasks/{task_id}/status/', tags=['Update tasks status'])
# async def update_tasks_status():
#     ...


