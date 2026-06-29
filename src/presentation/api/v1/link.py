from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse
from dependency_injector.wiring import Provide, inject

from src.application.dtos.link_dtos import CreateShortLinkRequest, ShortLinkResponse
from src.application.use_cases.create_short_link import CreateShortLink
from src.application.use_cases.get_link_stats import GetLinkStats
from src.application.use_cases.resolve_short_link import ResolveShortLink
from src.container import ApplicationContainer
from src.domain.exceptions.link_exceptions import LinkExpiredError, LinkNotFoundError

router = APIRouter(tags=["Shorten"])


@router.post("/link", response_model=ShortLinkResponse)
@inject
async def create_link(
    link_request: CreateShortLinkRequest,
    usecase: CreateShortLink = Depends(Provide[ApplicationContainer.create_short_link]),
):
    return await usecase.execute(link_request)


@router.get("/{code}")
@inject
async def redirect(
    code: str,
    usecase: ResolveShortLink = Depends(Provide[ApplicationContainer.resolve_short_link]),
):
    try:
        link = await usecase.execute(code)
    except LinkNotFoundError:
        return RedirectResponse(url="/")
    return RedirectResponse(url=link.original_url)


@router.get("/{code}/stats")
@inject
async def get_stats(
    code: str,
    usecase: GetLinkStats = Depends(Provide[ApplicationContainer.get_link_stats]),
):
    return await usecase.execute(code)
