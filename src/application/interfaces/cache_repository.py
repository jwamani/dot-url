from abc import ABC, abstractmethod


class ICache(ABC):
    @abstractmethod
    async def get(self, key: str) -> str|None:
        pass
    
    @abstractmethod
    async def set(self, key: str, value: str, ttl: int) -> None:
        pass
    
    @abstractmethod
    async def delete(self, key: str) -> None: pass
    @abstractmethod
    async def increment(self, key: str, ttl: int) -> int: pass # for rate-limiting