import uuid
from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, String, Text, func, UUID, Index, text, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.database.base import Base


class ShortLink(Base):
    __tablename__ = "short_links"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
    )
    short_code: Mapped[str] = mapped_column(String(10), unique=True, nullable=False)
    original_url: Mapped[str] = mapped_column(Text, nullable=False)
    is_active: Mapped[bool] = mapped_column(
        Boolean, default=True, nullable=False, server_default="TRUE"
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    expires_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True, default=None
    )

    __table_args__ = (
        Index(
            "ix_short_links_short_code", "short_code", unique=True
        ),  # most queried column on redirects
        Index("ix_short_links_user_id", "user_id"),  # all links for a user
        Index(
            "ix_short_links_user_created", "user_id", "created_at"
        ),  # composite index during pagination
        Index(
            "ix_short_links_active_code",
            "short_code",
            postgresql_where=text("is_active = TRUE"),
        ),
    )
