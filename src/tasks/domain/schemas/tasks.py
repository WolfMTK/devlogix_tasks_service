from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    """Базовая схема задач."""
    name: str | None = Field(None, description='Название задачи')
    description: str | None = Field(None, description='Описание задачи')


class TaskCreate(TaskBase):
    """Схема создания задач"""
    name: str = Field(..., description='Название задачи')
    user_id: int = Field(..., description='Индентификатор пользователя')


class TaskUpdate(TaskBase):
    """Схема обновления задач"""
    users: list[int] | None = Field(
        None, description='Список индентификаторов пользователей'
    )


class TaskGet(TaskBase):
    """Схема получения задач"""
    users: list[int] | None = Field(
        None,
        description='Список индентификаторов пользователей'
    )
