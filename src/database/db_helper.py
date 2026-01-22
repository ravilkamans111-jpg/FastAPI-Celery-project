from asyncio import current_task
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
    AsyncSession,
)
from src.core.config import settings


class DatabaseHelper:
    def __init__(self, url: str, echo: bool):
        self.engine = create_async_engine(url=url, echo=echo)
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            expire_on_commit=False,
            autocommit=False,
        )

    def get_scoped_session(self) -> async_scoped_session:
        return async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )

    async def session_dependency(self) -> AsyncGenerator[AsyncSession, None]:
        scoped: async_scoped_session = self.get_scoped_session()
        async with scoped() as session:  # <- гарантирует AsyncSession
            try:
                yield session
                await session.commit()  # commit автоматически
            except:
                await session.rollback()  # rollback при ошибке
                raise

# экземпляр для всего проекта
db_help = DatabaseHelper(url=settings.db_url, echo=settings.echo)
