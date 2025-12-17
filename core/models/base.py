from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr
from sqlalchemy.testing.schema import mapped_column


""" Задаем имя БД """


class Base(DeclarativeBase):
    """Абстрактный класс"""

    __abstract__ = True

    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id: Mapped[int] = mapped_column(primary_key=True)
