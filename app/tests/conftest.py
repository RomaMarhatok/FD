import os
import asyncio
import sys
import pytest
import pytest_asyncio
from yarl import URL
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from alembic.command import upgrade
from app.db.utils import temp_database, alembic_config_from_url

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


@pytest.fixture
def pg_url():
    if "DB_URL_PLACEHOLDER" not in os.environ:
        from dotenv import load_dotenv

        load_dotenv()
        os.environ.update({"TESTING": "True"})
    db_url = os.environ["DB_URL_PLACEHOLDER"]
    return URL(db_url)


@pytest.fixture
def temp_pg_database(pg_url):
    with temp_database(pg_url, suffix="pytest") as db_urL:
        yield db_urL


@pytest.fixture
def migrated_temp_pg_database(temp_pg_database):
    config = alembic_config_from_url(temp_pg_database)
    upgrade(config, "head")
    yield temp_pg_database


@pytest.fixture
def migrated_pg_sync_session(migrated_temp_pg_database) -> Session:
    engine = create_engine(migrated_temp_pg_database)
    try:
        session_factory = sessionmaker(engine, expire_on_commit=False)
        session: Session = session_factory()
        yield session
    finally:
        session.close()


@pytest_asyncio.fixture
async def migrated_pg_async_session(migrated_temp_pg_database) -> AsyncSession:
    engine = create_async_engine(migrated_temp_pg_database, echo=True)
    session_factory = async_sessionmaker(engine, expire_on_commit=False)
    try:
        async_session = session_factory()
        yield async_session
    finally:
        await async_session.close()
