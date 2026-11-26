from starlette import status


class AppException(Exception):
    status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail: str ='Internal Server Error'

    def __init__(self, detail: str | None = None) -> None:
        self.detail = detail if detail is not None else self.detail