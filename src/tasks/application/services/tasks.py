from tasks.application.protocols.unit_of_work import UoW

from tasks.domain.schemas import TaskCreate, TaskGet


class TaskService:
    async def create_task(self, uow: UoW, task: TaskCreate) -> TaskGet:
        """Создание задачи."""
        async with uow:
            task = await uow.tasks.add_one(**task.model_dump())
            await uow.commit()
            return task.to_read_model()

    async def get_task(self, uow: UoW, user_id: int, task_id: int) -> TaskGet:
        """Получение задачи."""

    async def get_tasks(self, uow: UoW, user_id: int) -> list[TaskGet]:
        """Получение задач."""
        async with uow:
            ...

    async def update_task(
            self, uow: UoW, user_id: int, task_id: int
    ) -> TaskGet:
        """Обновление задач."""
        async with uow:
            ...

    async def delete_task(self, uow: UoW, user_id: int, task_id: int) -> None:
        """Удаление задач."""
        async with uow:
            ...
