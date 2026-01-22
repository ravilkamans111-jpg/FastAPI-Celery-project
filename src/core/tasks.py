from time import sleep
from src.celery.celery_app import celery_app
from src.models.task import StatusEnum

""" Таска для Celery"""


@celery_app.task(name="tasks.process_task")
def process_task(task_id: int):
    sleep(5)
    from src.celery.celery_session import SessionLocal
    from models import Tasks

    session = SessionLocal()
    try:
        task = session.get(Tasks, task_id)
        if not task:
            return

        task.status = StatusEnum.DONE
        session.commit()

    finally:
        session.close()
