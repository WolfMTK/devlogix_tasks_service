from fastapi import FastAPI

from tasks.api import routers


def create_app() -> FastAPI:
    app = FastAPI()

    for router in routers:
        app.include_router(router)

    return app


app = create_app()
