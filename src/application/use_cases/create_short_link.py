from datetime import datetime

from src.application.interfaces.id_gen_repository import AbstractIdGenerator
from src.application.dtos.link_dtos import CreateShortLinkRequest, ShortLinkResponse

class CreateShortLink:
    async def execute(self, request: CreateShortLinkRequest, id_generator: AbstractIdGenerator|None = None, ):
        return ShortLinkResponse(
            id=1,
            user_id=1,
            original_url=request.original_url,
            click_count=3,
            expires_at=datetime(2026, 6, 29),
            created_at=datetime(2026, 6, 27)
        ).model_dump()
