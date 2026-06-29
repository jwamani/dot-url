from abc import ABC, abstractmethod

from src.application.interfaces.link_repository import IShortLinkRepository
from src.application.interfaces.user_repository import IUserRepository


class AbstractUnitOfWork(ABC):
    @property
    @abstractmethod
    def links(self) -> IShortLinkRepository: ...

    @property
    @abstractmethod
    def users(self) -> IUserRepository: ...

    @abstractmethod
    async def __aenter__(self) -> "AbstractUnitOfWork": ...

    @abstractmethod
    async def __aexit__(self, *args) -> None: ...

    @abstractmethod
    async def commit(self) -> None: ...

    @abstractmethod
    async def rollback(self) -> None: ...
