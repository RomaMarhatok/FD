import pytest
from sqlalchemy import text
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


def insert_characteristics(
    ref: str,
    weight: float,
    height: float,
    age: int,
    sex: str,
    eyes_color: str,
    hairs_color: str,
    nationality: str,
    session: Session,
):
    session.execute(
        text(
            f"""INSERT INTO characteristics(ref,weight,height,age,sex,eyes_color,hairs_color,nationality)
            VALUES('{ref}',{weight},{height},{age},'{sex}','{eyes_color}','{hairs_color}','{nationality}')"""
        )
    )


def insert_dossier(
    ref: str,
    history: str,
    social_status: str,
    marriage_status: str,
    session: Session,
):
    session.execute(
        text(
            f"""INSERT INTO dossier(ref,history,social_status,marriage_status)
        VALUES('{ref}','{history}','{social_status}','{marriage_status}')"""
        )
    )
