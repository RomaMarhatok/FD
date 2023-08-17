from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from app.config import settings


@asynccontextmanager
async def get_async_session():
    engine = create_async_engine(settings.DB_URL)
    async_session_factory = async_sessionmaker(engine)
    try:
        session = async_session_factory()
        yield session
    except Exception:
        await session.rollback()
    finally:
        await session.close()
        await engine.dispose()
