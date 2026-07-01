from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.application.interfaces.unit_of_work import AbstractUnitOfWork
from src.infrastructure.repositories.link_repository import ShortLinkRepository
from src.infrastructure.repositories.user_repository import UserRepository


class UnitOfWork(AbstractUnitOfWork):
    def __init__(self, session_factory: async_sessionmaker) -> None:
        self._session: AsyncSession = session_factory()

    async def __aenter__(self) -> AbstractUnitOfWork:
        self.links = ShortLinkRepository(self._session)
        self.users = UserRepository(self._session)
        return self

    async def __aexit__(self,exc_type, *args) -> None:
        if exc_type is not None:
            await self.rollback()
        else: 
            await self.commit()
        await self._session.close()

    async def commit(self) -> None:
        await self._session.commit()

    async def rollback(self) -> None:
        await self._session.rollback()
