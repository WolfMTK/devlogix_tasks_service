from pydantic import BaseModel, Field


class UserBase(BaseModel):
    """Базовая схема пользователей"""
    user_id: int | None = Field(
        None,
        description='Индентификатор пользователя'
    )


class UserGet(UserBase):
    """Схема получения пользователя."""
