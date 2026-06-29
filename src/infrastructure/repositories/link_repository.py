from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.interfaces.link_repository import IShortLinkRepository
from src.domain.entities.short_link import ShortLink
from src.infrastructure.models.short_link import ShortLink as ShortLinkModel


class ShortLinkRepository(IShortLinkRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create_link(self, link: ShortLink) -> ShortLink:
        model = ShortLinkModel(
            user_id=link.user_id,
            short_code=link.short_code,
            original_url=link.original_url,
            click_count=link.click_count,
            expires_at=link.expires_at,
        )
        self._session.add(model)
        await self._session.flush()
        return ShortLink(
            id=model.id,
            user_id=model.user_id,
            scode=model.short_code,
            original_url=model.original_url,
            click_count=model.click_count,
            created_at=model.created_at,
            expires_at=model.expires_at,
        )

    async def get_by_code(self, code: str) -> ShortLink | None:
        result = await self._session.execute(
            select(ShortLinkModel).where(ShortLinkModel.short_code == code)
        )
        model = result.scalar_one_or_none()
        if model is None:
            return None
        return ShortLink(
            id=model.id,
            user_id=model.user_id,
            scode=model.short_code,
            original_url=model.original_url,
            click_count=model.click_count,
            created_at=model.created_at,
            expires_at=model.expires_at,
        )

    async def get_by_user(self, user_id: int) -> list[ShortLink]:
        result = await self._session.execute(
            select(ShortLinkModel).where(ShortLinkModel.user_id == user_id)
        )
        models = result.scalars().all()
        return [
            ShortLink(
                id=m.id,
                user_id=m.user_id,
                scode=m.short_code,
                original_url=m.original_url,
                click_count=m.click_count,
                created_at=m.created_at,
                expires_at=m.expires_at,
            )
            for m in models
        ]

    async def delete_link(self, code: str) -> None:
        result = await self._session.execute(
            select(ShortLinkModel).where(ShortLinkModel.short_code == code)
        )
        model = result.scalar_one_or_none()
        if model:
            await self._session.delete(model)

    async def increment_clicks(self, code: str) -> None:
        result = await self._session.execute(
            select(ShortLinkModel).where(ShortLinkModel.short_code == code)
        )
        model = result.scalar_one_or_none()
        if model:
            model.click_count += 1
            await self._session.flush()
