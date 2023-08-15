from sqlalchemy import select, text
from sqlalchemy.orm import Session
from app.domain.person.dossier.hobbies import Hobbies


def test_hobby_can_read(migrated_pg_sync_session: Session):
    migrated_pg_sync_session.execute(
        text("INSERT INTO hobby(ref,description) VALUES('ref-1','description-1')")
    )
    stmt = select(Hobbies)
    received = migrated_pg_sync_session.execute(stmt).scalar()
    expected = Hobbies("ref-1", "description-1")
    assert received == expected


def test_hobby_can_write(migrated_pg_sync_session: Session):
    expected = Hobbies("ref-1", "description-1")
    migrated_pg_sync_session.add(expected)
    migrated_pg_sync_session.commit()
    stmt = select(Hobbies)
    received = migrated_pg_sync_session.execute(stmt).scalar()
    assert expected == received
