from abc import ABC, abstractmethod

class IApiKeyGenRepository(ABC):
    @abstractmethod
    def generate(self, length: int = 32) -> str:
        """Generate a new API key"""
        pass
    @abstractmethod
    def hash_key(self, api_key: str) -> str:
        """Hash the api key for secure storage"""
        pass
    
    @abstractmethod
    def verify_key(self, api_key: str, hashed_key: str) -> bool:
        """Verify if the provided api key matches the hashed key"""
        pass