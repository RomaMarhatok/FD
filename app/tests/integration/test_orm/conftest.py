import pytest
from sqlalchemy.orm import sessionmaker, Session


@pytest.fixture
def pg_sync_session(pg_sync_engine) -> Session:
    try:
        session: Session = sessionmaker(pg_sync_engine, expire_on_commit=False)()
        yield session
    finally:
        session.close()


@pytest.fixture
def migrated_pg_sync_session(migrated_pg_sync_engine) -> Session:
    try:
        session: Session = sessionmaker(
            migrated_pg_sync_engine, expire_on_commit=False
        )()
        yield session
    finally:
        session.close()
