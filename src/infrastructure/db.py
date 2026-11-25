from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, async_sessionmaker, AsyncSession

from src.config import settings

engine: AsyncEngine = create_async_engine(
    str(settings.postgres_url),
    pool_pre_ping=True,
    hide_parameters=True,
    echo=False,
)

SessionFactory = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)