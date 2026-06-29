"""absract classes for the short links"""

from abc import ABC, abstractmethod

from ...domain.entities.short_link import ShortLink

class IShortLinkRepository(ABC):
    @abstractmethod
    async def create_link(self, link: ShortLink) -> ShortLink:
        """Create a new short link"""
        pass
    
    @abstractmethod
    async def get_by_code(self, code: str) -> ShortLink|None:
        """Get a short link by its code"""
        pass
    
    @abstractmethod
    async def get_by_user(self, user_id: int) -> list[ShortLink]:
        """Get all short links for a user"""
        pass
    
    @abstractmethod
    async def delete_link(self, code: str) -> None:
        """Delete a short link by its code"""
        pass
    
    @abstractmethod
    async def increment_clicks(self, code: str) -> None:
        """Increment the click count for a short link"""
        pass