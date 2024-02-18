from collections import Generator

from sqlalchemy.orm import Mapped, mapped_column, relationship

from tasks.domain.models.association_tables import users_tasks
from tasks.infrastructure.db import Base

from tasks.domain.schemas import UserGet


class User(Base):
    """Модель пользователей."""
    user_id: Mapped[int] = mapped_column(nullable=False)
    tasks: Mapped[list['Task']] = relationship(
        secondary=users_tasks,
        back_populates='users'
    )

    def to_read_model(self) -> UserGet:
        return UserGet(user_id=self.user_id)
