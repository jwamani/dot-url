from pydantic import BaseModel, Field
from datetime import datetime


class CreateShortLinkRequest(BaseModel):
    """request dto for creating a short link"""
    
    original_url: str = Field(..., description="The url to be shortened")
    user_id: int|None = Field(None, description="Owner of the shortlink")



class ShortLinkResponse(BaseModel):
    id: int
    user_id: int
    original_url: str
    click_count: int
    expires_at: datetime
    created_at: datetime