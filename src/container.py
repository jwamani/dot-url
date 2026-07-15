from dependency_injector import containers, providers

from src.application.use_cases import (
    CreateShortLink,
    GetLinkStats,
    ResolveShortLink,
    CreateUser
)
from src.infrastructure.config import Settings
from src.infrastructure.database.connection import create_engine, create_session_factory
from src.infrastructure.database.unit_of_work import UnitOfWork
from src.infrastructure.id_generation.nanoid_gen import NanoidIdGenerator
from src.infrastructure.repositories.api_key_repo_impl import APIKeyGen


class Container(containers.DeclarativeContainer):
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
    api_key_generator = providers.Singleton(APIKeyGen) 

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
    
    create_user = providers.Factory(
        CreateUser,
        uow=uow,
        api_key_generator=api_key_generator
    )
