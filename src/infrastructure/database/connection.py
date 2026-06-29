from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine


def create_engine(db_url: str):
    return create_async_engine(db_url)


def create_session_factory(engine):
    return async_sessionmaker(engine, expire_on_commit=False)
