from fastapi import FastAPI
from starlette.responses import JSONResponse


def get_app() -> FastAPI:

    app = FastAPI(
        docs_url='/docs',
        openapi_url='/openapi.json',
        default_response_class=JSONResponse,
    )

    return app
