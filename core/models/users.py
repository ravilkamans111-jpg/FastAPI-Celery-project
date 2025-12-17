
from typing import TYPE_CHECKING
from core.models.base import Base
from datetime import datetime
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship


''' Алхимия для пользователей'''


if TYPE_CHECKING:
    from .task import Tasks


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    email: Mapped[str] = mapped_column(
        String,
        unique=True,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    tasks: Mapped[list["Tasks"]] = relationship(
        "Tasks",
        back_populates="user",
        cascade="all, delete-orphan"
    )

