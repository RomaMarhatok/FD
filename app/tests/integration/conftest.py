import pytest
from app.db.utils import alembic_config_from_url


@pytest.fixture
def alembic_config(temp_pg_database):
    return alembic_config_from_url(temp_pg_database)
