from fastapi import APIRouter, Depends

from src.application.use_cases.create_short_link import CreateShortLink
from src.application.dtos.link_dtos import CreateShortLinkRequest, ShortLinkResponse

router = APIRouter(tags=["Shorten"])


@router.post("/link", response_model=ShortLinkResponse)
async def get_code(link_request: CreateShortLinkRequest, usecase: CreateShortLink = Depends()):
    return await usecase.execute(link_request)