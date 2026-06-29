from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncEngine


def create_engine(db_url: str):
    return create_async_engine(db_url, pool_pre_ping=True, pool_recycle=3600)


def create_session_factory(engine: AsyncEngine):
    return async_sessionmaker(engine, expire_on_commit=False)
