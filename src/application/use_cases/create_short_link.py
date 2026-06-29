from datetime import datetime, timezone as tz

from src.application.dtos.link_dtos import CreateShortLinkRequest, ShortLinkResponse
from src.application.interfaces.id_gen_repository import AbstractIdGenerator
from src.application.interfaces.unit_of_work import AbstractUnitOfWork
from src.domain.entities.short_link import ShortLink


class CreateShortLink:
    def __init__(self, uow: AbstractUnitOfWork, id_generator: AbstractIdGenerator) -> None:
        self._uow = uow
        self._id_generator = id_generator

    async def execute(self, request: CreateShortLinkRequest) -> ShortLinkResponse:
        code = self._id_generator.generate()

        async with self._uow as uow:
            link = ShortLink(
                id=None,
                user_id=request.user_id,
                scode=code,
                original_url=str(request.original_url),
                click_count=0,
                created_at=datetime.now(tz.utc),
            )
            created = await uow.links.create_link(link)
            await uow.commit()

        return ShortLinkResponse(
            id=created.id,
            user_id=created.user_id,
            original_url=created.original_url,
            click_count=created.click_count,
            expires_at=created.expires_at,
            created_at=created.created_at,
        )
