from dataclasses import dataclass
from datetime import datetime, timezone as tz
"""id,code,original_url,created_at,click_count"""

class ShortCode:
    def __init__(self,id: int|None, scode: str, original_url: str, click_count: int, created_at: datetime|None ) -> None:
        self.id = id
        self.code = scode
        self.original_url = original_url
        self.click_count = click_count
        self.created_at = created_at or datetime.now(tz.utc)
