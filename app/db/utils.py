import uuid
import os
import pathlib
from types import SimpleNamespace
from contextlib import contextmanager
from yarl import URL
from sqlalchemy_utils import create_database, drop_database
from alembic.config import Config
from app import __file__

PROJECT_PATH = pathlib.Path(__file__).parent.parent
project_name = PROJECT_PATH.name


def make_alembic_config(
    cmd_options: SimpleNamespace, base_path: str | None = PROJECT_PATH
) -> Config:
    if not os.path.isabs(cmd_options.config):
        cmd_options.config = os.path.join(base_path, cmd_options.config)
    config = Config(
        file_=cmd_options.config, ini_section=cmd_options.name, cmd_opts=cmd_options
    )
    config.set_main_option("script_location", os.path.join(base_path, cmd_options.name))
    if cmd_options.pg_url:
        config.set_main_option("sqlalchemy.url", cmd_options.pg_url)
    return config


def alembic_config_from_url(pg_url: str | None = None) -> Config:
    cmd_options = SimpleNamespace(
        config="alembic.ini",
        name="migrations",
        pg_url=pg_url,
        raiseerr=False,
        x=None,
    )
    return make_alembic_config(cmd_options)


@contextmanager
def temp_database(db_url: URL, suffix: str = "", **kwargs):
    tmp_db_name = ".".join([uuid.uuid4().hex, project_name, suffix])
    tmp_db_url = str(db_url.with_path(tmp_db_name))
    create_database(tmp_db_url, **kwargs)
    try:
        yield tmp_db_url
    finally:
        drop_database(tmp_db_url)
