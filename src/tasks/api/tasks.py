from fastapi import APIRouter

from tasks.api.dependencies import UoWDep
from tasks.application.services.tasks import TaskService
from tasks.domain.schemas import TaskCreate, TaskGet

router = APIRouter(prefix='tasks', tags=['tasks'])


@router.post(
    '/',
    response_model=TaskGet
)
async def create_task(task: TaskCreate, uow: UoWDep):
    return await TaskService().create_task(uow, task)


@router.get(
    '/',
    response_model=TaskGet
)
async def get_tasks(user_id, uow: UoWDep):
    return await TaskService().get_tasks(uow, user_id)


@router.get(
    '/{id}/',
    response_model=TaskGet
)
async def get_task(id: int, user_id: int, uow: UoWDep):
    return await TaskService().get_task(uow, user_id, id)


@router.patch(
    '/{id}/',
    response_model=TaskGet
)
async def update_task(id: int, user_id: int, uow: UoWDep):
    return await TaskService().update_task(uow, user_id, id)


@router.delete(
    '/{id}/',
    response_model=TaskGet
)
async def delete_task(id: int, user_id: int, uow: UoWDep):
    return await TaskService().delete_task(uow, user_id, id)
