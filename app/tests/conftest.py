import os
import pytest

from contextlib import contextmanager
from yarl import URL
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine
from alembic.command import upgrade
from app.db.utils import temp_database, alembic_config_from_url


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


@contextmanager
def init_engine(db_url, factory=None):
    try:
        engine = factory(db_url, echo=True)
        yield engine
    finally:
        engine.dispose()


@pytest.fixture
def pg_sync_engine(temp_pg_database):
    with init_engine(temp_pg_database, factory=create_engine) as engine:
        yield engine


@pytest.fixture
def migrated_temp_pg_database(temp_pg_database):
    config = alembic_config_from_url(temp_pg_database)
    upgrade(config, "head")
    yield temp_pg_database


@pytest.fixture
def migrated_pg_sync_engine(migrated_temp_pg_database):
    with init_engine(migrated_temp_pg_database, factory=create_engine) as engine:
        yield engine
