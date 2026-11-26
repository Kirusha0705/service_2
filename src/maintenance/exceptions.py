from starlette import status

from src.exceptions import AppException


class ObjectNotFoundException(AppException):
    status_code = status.HTTP_404_NOT_FOUND

    def __init__(self,detail: str | None) -> None:
        self.detail = detail