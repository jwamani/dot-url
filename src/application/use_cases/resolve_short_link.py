from src.domain.exceptions.link_exceptions import LinkExpiredError, LinkNotFoundError
from src.domain.entities.short_link import ShortLink


class ResolveShortLink:
    def __init__(self, uow) -> None:
        self._uow = uow

    async def execute(self, code: str) -> ShortLink:
        async with self._uow as uow:
            link = await uow.links.get_by_code(code)
            if link is None:
                raise LinkNotFoundError(f"Link '{code}' not found")
            if link.is_expired():
                raise LinkExpiredError(f"Link '{code}' has expired")
            await uow.links.increment_clicks(code)
            await uow.commit()
        return link
