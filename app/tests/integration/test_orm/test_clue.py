from sqlalchemy import text, select
from sqlalchemy.orm import Session
from app.domain.detective_history.clue import Clue


def test_clue_can_read(migrated_pg_sync_session: Session):
    migrated_pg_sync_session.execute(
        text("""INSERT INTO clue(ref,description) VALUES('ref-1','clue description')""")
    )
    stmt = select(Clue)
    received = migrated_pg_sync_session.execute(stmt).scalar()
    expected = Clue(ref="ref-1", description="clue description")
    assert received == expected


def test_clue_can_save(migrated_pg_sync_session: Session):
    clue = Clue(ref="ref-1", description="clue description")
    migrated_pg_sync_session.add(clue)
    migrated_pg_sync_session.commit()
    stmt = select(Clue)
    received = migrated_pg_sync_session.execute(stmt).scalar()
    assert clue == received
