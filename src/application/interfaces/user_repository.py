
from abc import ABC, abstractmethod

from ...domain.entities.user import User


class IUserRepository(ABC):
    @abstractmethod
    async def create_user(self, user: User) -> User:
        """Create a new user"""
        pass

    @abstractmethod
    async def get_user_by_email(self, email: str) -> User|None:
        """Get a user by their email"""
        pass

    @abstractmethod
    async def get_user_by_id(self, user_id: int) -> User|None:
        """Get a user by their ID"""
        pass
    
    @abstractmethod
    async def get_user_by_api_key(self, api_key: str) -> User|None:
        """Get a user by their API key"""
        pass
    
    @abstractmethod
    async def update_user(self, user) -> User:
        """Update a user's information"""
        pass
    
    @abstractmethod
    async def get_all(self) -> list[User]:
        """Get all users"""
        pass