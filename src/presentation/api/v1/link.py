from fastapi import APIRouter, Depends, status
from fastapi.responses import RedirectResponse
from dependency_injector.wiring import Provide, inject

from src.application.dtos.link_dtos import CreateShortLinkRequest, ShortLinkResponse
from src.application.use_cases.create_short_link import CreateShortLink
from src.application.use_cases.get_link_stats import GetLinkStats
from src.application.use_cases.resolve_short_link import ResolveShortLink
from src.container import Container
from src.domain.exceptions.link_exceptions import LinkExpiredError, LinkNotFoundError

router = APIRouter(tags=["Shorten"])


@router.post("/link", response_model=ShortLinkResponse, status_code=status.HTTP_201_CREATED)
@inject
async def create_link(
    link_request: CreateShortLinkRequest,
    usecase: CreateShortLink = Depends(Provide[Container.create_short_link]),
):
    return await usecase.execute(link_request)


@router.get("/{code}")
@inject
async def redirect(
    code: str,
    usecase: ResolveShortLink = Depends(Provide[Container.resolve_short_link]),
):
    try:
        link = await usecase.execute(code)
    except LinkNotFoundError:
        return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)
    except LinkExpiredError:
        return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)
    return RedirectResponse(url=link.original_url, status_code=status.HTTP_302_FOUND)


@router.get("/{code}/stats", response_model=ShortLinkResponse)
@inject
async def get_stats(
    code: str,
    usecase: GetLinkStats = Depends(Provide[Container.get_link_stats]),
):
    try:
        return await usecase.execute(code)
    except LinkNotFoundError:
        from fastapi.responses import JSONResponse
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"detail": "Link not found"},
        )
