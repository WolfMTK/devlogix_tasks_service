from tasks.application.protocols.repository import SQLAlchemyRepository
from tasks.domain.models.tasks import Task


class TasksRepository(SQLAlchemyRepository):
    model = Task
