"""user entity"""
from datetime import datetime, timezone as tz

class User:
    def __init__(self, email: str, password: str, api_key: str, created_at: datetime|None, is_active: bool = True, updated_at: datetime|None = None, id: int|None=None) -> None:
        self.id = id
        self.email = email
        self.password = password
        self.api_key = api_key
        self.is_active = is_active
        self.created_at = created_at or datetime.now(tz.utc)
        self.updated_at = updated_at or datetime.now(tz.utc)
    
    
    def deactivate(self) -> None:
        """Deactivate the user account."""
        self.is_active = False
        self.updated_at = datetime.now(tz.utc)
    
    @staticmethod
    def generate_api_key():
        pass
    
    def has_permission(self) -> bool:
        return False
    
    