from tasks.application.protocols.unit_of_work import UoW


class TaskService:
    async def create_task(self, uow: UoW) -> None:
        """Создание задачи."""

    async def get_task(self, uow: UoW):
        """Получение задачи."""

    async def get_tasks(self, uow: UoW):
        """Получение задач."""

    async def update_task(self, uow: UoW):
        """Обновление задач."""

    async def delete_task(self, uow: UoW) -> None:
        """Удаление задач."""
