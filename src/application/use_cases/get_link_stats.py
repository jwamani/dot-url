from src.application.dtos.link_dtos import ShortLinkResponse
from src.domain.exceptions.link_exceptions import LinkNotFoundError
from src.application.interfaces.unit_of_work import AbstractUnitOfWork


class GetLinkStats:
    def __init__(self, uow: AbstractUnitOfWork) -> None:
        self._uow = uow

    async def execute(self, code: str) -> ShortLinkResponse:
        async with self._uow as uow:
            link = await uow.links.get_by_code(code)
            if link is None:
                raise LinkNotFoundError(f"Link '{code}' not found")
        return ShortLinkResponse(
            id=link.id,
            user_id=link.user_id,
            original_url=link.original_url,
            click_count=link.click_count,
            expires_at=link.expires_at,
            created_at=link.created_at,
        )
