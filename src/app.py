from fastapi import FastAPI
from sqlalchemy.exc import SQLAlchemyError
from starlette.responses import JSONResponse

from src.exceptions import AppException
from src.exceptions_handler import unexpected_exception_handler, app_exception_handler, handle_db_error
from src.infrastructure.logger import RequestIDMiddleware
from src.maintenance.router import router as maintenance_router


def get_app() -> FastAPI:

    app = FastAPI(
        docs_url='/docs',
        openapi_url='/openapi.json',
        default_response_class=JSONResponse,
    )
    app.add_middleware(RequestIDMiddleware)
    register_routers(app)
    app.add_exception_handler(Exception, unexpected_exception_handler)
    app.add_exception_handler(AppException, app_exception_handler)
    app.add_exception_handler(SQLAlchemyError, handle_db_error)

    return app


def register_routers(app: FastAPI) -> None:
    app.include_router(maintenance_router)
