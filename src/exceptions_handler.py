from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse

from src.exceptions import AppException
from src.infrastructure.logger import log
from src.schemas import ErrorResponse


async def unexpected_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    response = ErrorResponse(detail='Internal Server Error')

    log.error(
        "unexpected_exception",
        exception_type=type(exc).__name__,
        exc_info=exc,
    )

    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=response.model_dump(),
    )

async def app_exception_handler(request: Request, exc: AppException) -> JSONResponse:
    response = ErrorResponse(detail=exc.detail)

    return JSONResponse(
        status_code=exc.status_code,
        content=response.model_dump(),
    )

def handle_db_error(request: Request, exc: SQLAlchemyError, ) -> JSONResponse:
    response = ErrorResponse(detail='Internal Server Error')
    original_error = getattr(exc, "orig", None)
    sqlstate = getattr(original_error, "sqlstate", None)

    if isinstance(exc, IntegrityError) and sqlstate == "23505":
        response = ErrorResponse(detail="Unique conflict: Car already has the same date of maintenance")
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content=response.model_dump(),
        )

    if isinstance(exc, IntegrityError) and sqlstate == "23514":
        response = ErrorResponse(detail="Date error: last date greater than next date")
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            content=response.model_dump(),
        )

    log.error(
        "unexpected_db_error",
        exception_type=type(exc).__name__,
        exc_info=exc,
        sqlstate=sqlstate
    )


    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=response.model_dump()
    )