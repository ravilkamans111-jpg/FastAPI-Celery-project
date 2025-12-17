from celery import Celery

"""Celery приложение"""

celery_app = Celery(
    "core",
    broker="amqp://guest:guest@localhost:5672//",
    backend="rpc://",
    brocker_connection_retry_or_startup=True,
)

celery_app.autodiscover_tasks(
    [
        "core",
    ]
)
