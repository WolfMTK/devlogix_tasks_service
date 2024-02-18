from fastapi import APIRouter

from tasks.api.dependencies import UoWDep
from tasks.application.services.tasks import TaskService
from tasks.domain.schemas.tasks import TaskCreate, TaskGet, TaskUpdate

router = APIRouter(prefix='tasks', tags=['tasks'])


@router.post(
    '/',
    response_model=TaskGet
)
async def create_task(uow: UoWDep, task: TaskCreate):
    return await TaskService().create_task(uow)


@router.get(
    '/',
    response_model=TaskGet
)
async def get_tasks(uow: UoWDep):
    return await TaskService().get_tasks(uow)


@router.get(
    '/{id}/',
    response_model=TaskGet
)
async def get_task(id: int, uow: UoWDep):
    return await TaskService().get_task(uow)


@router.patch(
    '/{id}/',
    response_model=TaskGet
)
async def update_task(id: int, uow: UoWDep):
    return await TaskService().update_task(uow)


@router.delete(
    '/{id}/',
    response_model=TaskGet
)
async def delete_task(id: int, uow: UoWDep):
    return await TaskService().delete_task(uow)
