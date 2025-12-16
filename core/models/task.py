from core.mixin import UpdatedAtMixin, CreatedAtMixin
import enum
from sqlalchemy import DateTime, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.models.base import Base
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .users import User


class StatusEnum(str, enum.Enum):
    PENDING = 'pending'
    IN_PROGRESS = 'in progress'
    DONE = 'done'


class Tasks(Base, UpdatedAtMixin, CreatedAtMixin):
    __tablename__ = "Tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str | None] = mapped_column(String, nullable=True)
    status: Mapped[StatusEnum] = mapped_column(String, default=StatusEnum.PENDING)

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    user: Mapped["User"] = relationship(
        "User",
        back_populates="tasks"
    )
