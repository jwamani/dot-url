from abc import ABC, abstractmethod

class IApiKeyGenRepository(ABC):
    @abstractmethod
    def generate(self, length: int = 32) -> str:
        """Generate a new API key"""
        pass