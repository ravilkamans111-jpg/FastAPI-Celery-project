from asyncio import current_task
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
)
from core.config import settings


class DatabaseHelper:
    """
    engine = create_async_engine('sqlite+aiosqlite:///users_1.db')
    new_session = async_sessionmaker(engine, expire_on_commit=False)
    """

    def __init__(self, url: str, echo: bool):
        # создается асинхронный движок, из которого потом делаются сессии
        self.engine = create_async_engine(url=url, echo=echo)
        # создает фабрику сессий чтобы потом делать объекты AsyncSession
        self.session_factory = async_sessionmaker(
            # сессии будут работать через созданный ранее движок
            bind=self.engine,
            autoflush=False,
            expire_on_commit=False,
            autocommit=False,
        )

    """ Возвращает объект сессии для работы с БД  """

    def get_scoped_session(self):
        return async_scoped_session(
            session_factory=self.session_factory,
            # привязываем к текущей задаче
            scopefunc=current_task,
        )

    """ Создан для использования как dependency в FastAPI (через Depends)  """

    async def session_dependency(self):
        # берем scope-сессию для работы с текущей задачей
        session = self.get_scoped_session()

        """ Выдаем по одной сессии для текущей задачи """
        yield session
        await session.remove()


""" Экземпляр класс для работы в коде """
db_help = DatabaseHelper(url=settings.db_url, echo=settings.echo)
