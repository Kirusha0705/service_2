from fastapi import FastAPI
from starlette.responses import JSONResponse

from src.maintenance.router import router as maintenance_router


def get_app() -> FastAPI:

    app = FastAPI(
        docs_url='/docs',
        openapi_url='/openapi.json',
        default_response_class=JSONResponse,
    )
    register_routers(app)

    return app


def register_routers(app: FastAPI) -> None:
    app.include_router(maintenance_router)
