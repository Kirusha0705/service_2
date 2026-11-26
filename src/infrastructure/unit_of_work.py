from types import TracebackType
from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker


class UnitOfWork:

    def __init__(
            self,
            session_factory: async_sessionmaker[AsyncSession],
            read_only: bool = False
    ) -> None:
        self.session_factory = session_factory
        self.read_only = read_only

    async def __aenter__(self) -> 'UnitOfWork':
        self.session = self.session_factory()
        if not self.read_only:
            self.transaction = await self.session.begin()

        return self

    async def __aexit__(
            self,
            exc_type: Type[BaseException] | None,
            exc_val: BaseException | None,
            exc_tb: TracebackType | None
    ) -> None:
        try:
            if exc_type:
                await self.session.rollback()
            elif self.read_only:
                await self.session.rollback()
            else:
                await self.session.commit()
        finally:
            await self.session.close()

