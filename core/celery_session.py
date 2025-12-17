from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

''' Синхронная сессия для Celery '''

engine = create_engine(
    "sqlite:///test.db",
    pool_pre_ping=True,
)


SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)