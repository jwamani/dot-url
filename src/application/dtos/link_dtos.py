from pydantic import BaseModel, Field, HttpUrl
from datetime import datetime


class CreateShortLinkRequest(BaseModel):
    original_url: HttpUrl
    user_id: int | None = Field(None, description="Owner of the shortlink")


class ShortLinkResponse(BaseModel):
    id: int
    user_id: int | None
    original_url: str
    click_count: int
    expires_at: datetime | None = None
    created_at: datetime