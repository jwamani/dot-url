from dependency_injector import containers, providers

from src.application.use_cases.create_short_link import CreateShortLink
from src.application.use_cases.get_link_stats import GetLinkStats
from src.application.use_cases.resolve_short_link import ResolveShortLink
from src.infrastructure.config import Settings
from src.infrastructure.database.connection import create_engine, create_session_factory
from src.infrastructure.database.unit_of_work import UnitOfWork
from src.infrastructure.id_generation.nanoid_gen import NanoidIdGenerator


class ApplicationContainer(containers.DeclarativeContainer):
    config = providers.Singleton(Settings)

    engine = providers.Singleton(create_engine, config.provided.db_url)

    session_factory = providers.Singleton(
        create_session_factory, engine=engine
    )

    uow = providers.Factory(
        UnitOfWork,
        session_factory=session_factory,
    )

    id_generator = providers.Singleton(NanoidIdGenerator)

    create_short_link = providers.Factory(
        CreateShortLink,
        uow=uow,
        id_generator=id_generator,
    )

    resolve_short_link = providers.Factory(
        ResolveShortLink,
        uow=uow,
    )

    get_link_stats = providers.Factory(
        GetLinkStats,
        uow=uow,
    )
