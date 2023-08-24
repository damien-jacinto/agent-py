import threading
from typing import List

from fastapi import FastAPI, Request
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from api import router
from api.default.default import default_router
from core.config import config
from core.exceptions import CustomException

from monitor import MonitorTask


def init_routers(app: FastAPI) -> None:
    app.include_router(default_router)
    app.include_router(router)


def init_listeners(app: FastAPI) -> None:
    # Exception handler
    @app.exception_handler(CustomException)
    async def custom_exception_handler(request: Request, exc: CustomException):
        return JSONResponse(
            status_code=exc.code,
            content={"error_code": exc.error_code, "message": exc.message},
        )

    @app.on_event("startup")
    def on_start_up():
        thread = threading.Thread(target=app.state.monitortask.monitor, daemon=True)
        thread.start()


def make_middleware() -> List[Middleware]:
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        ),
    ]
    return middleware


def create_app() -> FastAPI:
    monitortask = MonitorTask()
    app = FastAPI(
        title=config.TITLE,
        description=config.description,
        version=config.version,
        docs_url=None if config.ENV == "production" else "/docs",
        redoc_url=None if config.ENV == "production" else "/redoc",
        middleware=make_middleware(),
    )
    app.state.monitortask = monitortask
    app.state.version = config.version
    init_routers(app=app)
    init_listeners(app=app)
    return app


app = create_app()
