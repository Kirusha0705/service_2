from typing import Any
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepository:

    model = None

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def read_one_or_none(self, **filters):
        stmt = (select(self.model).
                filter_by(**filters).
                order_by(self.model.last_date_maintenance.desc()).
                limit(1))

        result = await self.session.execute(stmt)

        return result.scalar_one_or_none()


    async def create(self, data):
        self.session.add(data)
        await self.session.flush()
        return data
