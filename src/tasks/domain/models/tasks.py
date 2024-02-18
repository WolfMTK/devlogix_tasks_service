from sqlalchemy.orm import Mapped, mapped_column, relationship

from tasks.domain.models.association_tables import users_tasks
from tasks.infrastructure.db import Base
from tasks.domain.schemas import TaskGet


class Task(Base):
    """Модель задач."""
    name: Mapped[str] = mapped_column(nullable=True)
    description: Mapped[str] = mapped_column(nullable=False)
    users: Mapped[list['User']] = relationship(
        secondary=users_tasks,
        back_populates='tasks',
        lazy='selectin'
    )

    def to_read_model(self) -> TaskGet:
        if not self.users:
            return TaskGet(
                name=self.name,
                description=self.description
            )
        return TaskGet(
            name=self.name,
            description=self.description,
            users=[user.to_read_model() for user in self.users]
        )
