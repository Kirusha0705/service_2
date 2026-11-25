from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepository:

    model = None

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def read(self, car_id: UUID):
        pass
        # stmt = (select(self.model).
        #         filter_by(car_id=car_id).)

    async def create(self):
        pass