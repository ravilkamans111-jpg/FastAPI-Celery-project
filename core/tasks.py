from time import sleep
from core.celery_app import celery_app
from core.models.task import StatusEnum, Tasks
from .models import db_help

''' Таска для Celery'''

@celery_app.task(name='tasks.process_task')
def process_task(task_id: int):
    print('Мы в celery')
    sleep(5)
    from core.celery_session import SessionLocal
    from core.models import Tasks

    session = SessionLocal()
    try:
        task = session.get(Tasks, task_id)
        if not task:
            return

        task.status = StatusEnum.DONE
        session.commit()

    finally:
        session.close()
