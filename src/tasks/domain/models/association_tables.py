from sqlalchemy import Table, Column, ForeignKey

from tasks.infrastructure.db import Base

users_tasks = Table(
    'users_tasks',
    Base,
    Column('task_id', ForeignKey('task.id')),
    Column('user_id', ForeignKey('user.id'))
)
