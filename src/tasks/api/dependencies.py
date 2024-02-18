from typing import Annotated

from fastapi import Depends

from tasks.application.protocols.unit_of_work import UnitOfWork, UoW
from tasks.infrastructure.db import async_session_maker


def connect_database() -> UnitOfWork:
    return UnitOfWork(async_session_maker)


UoWDep = Annotated[UoW, Depends(connect_database)]
