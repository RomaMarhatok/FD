from sqlalchemy import text, select
from sqlalchemy.orm import Session
from app.domain.person.dossier.motives import Motives


def test_motives_can_read(migrated_pg_sync_session: Session):
    migrated_pg_sync_session.execute(
        text("INSERT INTO motive(ref,description) VALUES('ref-1','description-1')")
    )
    stmt = select(Motives)
    received = migrated_pg_sync_session.execute(stmt).scalar()
    expected = Motives("ref-1", "description-1")
    assert received == expected


def test_motives_can_write(migrated_pg_sync_session: Session):
    expected = Motives("ref-1", "description-1")
    migrated_pg_sync_session.add(expected)
    migrated_pg_sync_session.commit()
    stmt = select(Motives)
    received = migrated_pg_sync_session.execute(stmt).scalar()
    assert expected == received
