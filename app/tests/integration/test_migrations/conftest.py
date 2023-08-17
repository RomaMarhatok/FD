import pytest
from sqlalchemy import create_engine
from app.db.utils import alembic_config_from_url


@pytest.fixture
def alembic_config(temp_pg_database):
    return alembic_config_from_url(temp_pg_database)


@pytest.fixture
def pg_sync_engine(temp_pg_database):
    try:
        engine = create_engine(temp_pg_database, echo=True)
        yield engine
    finally:
        engine.dispose()
