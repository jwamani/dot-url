from dataclasses import dataclass
from datetime import datetime, timezone as tz
"""id,code,original_url,created_at,click_count"""

class ShortLink:
    def __init__(self,id: int, user_id: int, scode: str, original_url: str, click_count: int, created_at: datetime|None, expires_at: datetime|None = None) -> None:
        self.id = id
        self.user_id = user_id
        self.short_code = scode
        self.original_url = original_url
        self.click_count = click_count
        self.created_at = created_at or datetime.now(tz.utc)
        self.expires_at: datetime|None = None
    
    def is_expired(self) -> bool:
        if self.expires_at is None:
            return False
        return datetime.now(tz.utc) > self.expires_at
    
    def increment_clicks(self) -> None:
        self.click_count += 1

    def __repr__(self) -> str:
        return f"<ShortCode(id={self.id}, code={self.short_code}, original_url={self.original_url})>"
