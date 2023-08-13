from alembic.config import Config
from alembic.command import upgrade
from sqlalchemy.engine.base import Engine
from alembic.runtime.migration import MigrationContext
from alembic.autogenerate import compare_metadata
from app.db.models.base import SqlAlchemyBaseModel


def test_migrations_up_to_date(alembic_config: Config, pg_sync_engine: Engine):
    upgrade(alembic_config, "head")
    ctx = MigrationContext.configure(connection=pg_sync_engine.connect())
    diff = compare_metadata(ctx, SqlAlchemyBaseModel.metadata)
    assert not diff
