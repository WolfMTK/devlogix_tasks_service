from sqlalchemy.orm import Mapped, mapped_column, relationship

from tasks.domain.models.association_tables import users_tasks
from tasks.infrastructure.db import Base


class Task(Base):
    """Модель задач."""
    name: Mapped[str] = mapped_column(nullable=True)
    description: Mapped[str] = mapped_column(nullable=False)
    users: Mapped[list['User']] = relationship(
        secondary=users_tasks,
        back_populates='tasks'
    )
