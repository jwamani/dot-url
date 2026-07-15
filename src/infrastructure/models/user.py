import uuid

from datetime import datetime, timezone as tz
from sqlalchemy import Boolean, DateTime, Integer, String, func, UUID, Index, text
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.database.base import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    api_key_hash: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
    
    __table_args__ = (
        Index("ix_users_email", "email", unique=True),
        Index("ix_users_api_key_hash", "api_key_hash", unique=True),
        # partial index for active users
        Index("ix_users_active", "is_active", postgresql_where=text("is_active = TRUE"))
    )
