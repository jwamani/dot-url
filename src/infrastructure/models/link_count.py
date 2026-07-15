import uuid

from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, Integer, String, Text, func, UUID, Index
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.database.base import Base

class LinkClick(Base):
    __tablename__ = "link_clicks"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    link_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("short_links.id", ondelete="CASCADE"),
        nullable=False,
    )
    clicked_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    # Optional analytics
    ip_hash: Mapped[str | None] = mapped_column(
        String(64), nullable=True
    )
    country: Mapped[str | None] = mapped_column(String(2), nullable=True)  # "US", "GB"
    user_agent: Mapped[str | None] = mapped_column(String(255), nullable=True)

    __table_args__ = (
        Index("ix_link_clicks_link_id", "link_id"),
        Index("ix_link_clicks_clicked_at", "clicked_at"),
        # Composite for "clicks per link over time" queries
        Index("ix_link_clicks_link_time", "link_id", "clicked_at"),
    )
