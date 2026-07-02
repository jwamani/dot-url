from pydantic import BaseModel, EmailStr, Field


class CreateUserRequest(BaseModel):
    email: EmailStr = Field(..., description="The user's email address")
    password: str = Field(..., min_length=8, description="The user's password")

class UserResponse(BaseModel):
    id: int = Field(..., description="The user's unique indentifier")
    email: EmailStr = Field(..., description="The user's email address")
    api_key: str = Field(..., description="The user's API key")
    is_active: bool = Field(..., description="Indicates if the user is active")
    created_at: str|None = Field(None, description="The date and time the user was created")
    updated_at: str|None = Field(None, description="The date and time the user was last updated")