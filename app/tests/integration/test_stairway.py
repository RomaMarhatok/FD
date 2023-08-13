import pytest
from alembic.config import Config
from alembic.command import upgrade, downgrade
from alembic.script import ScriptDirectory, Script
from app.db.utils import alembic_config_from_url


def get_revisions():
    config = alembic_config_from_url()
    revisions_dir = ScriptDirectory.from_config(config)
    revisions = list(revisions_dir.walk_revisions("base", "heads"))
    revisions.reverse()
    return revisions


@pytest.mark.parametrize("revision", get_revisions())
def test_stairway(alembic_config: Config, revision: Script):
    upgrade(alembic_config, revision.revision)
    downgrade(alembic_config, revision.revision)
    upgrade(alembic_config, revision.revision)
