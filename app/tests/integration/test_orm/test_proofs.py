from sqlalchemy import text, select
from sqlalchemy.orm import Session
from app.domain.detective_history.proofs import Proofs
from app.domain.detective_history.clue import Clue


def test_proofs_can_read(migrated_pg_sync_session: Session):
    migrated_pg_sync_session.execute(
        text(
            """INSERT INTO proof(ref,description) VALUES('proof-ref','proof descirption')"""
        )
    )
    expected = Proofs(ref="proof-ref", description="proof descirption", clues=set())
    stmt = select(Proofs)
    recieved = migrated_pg_sync_session.execute(stmt).scalar()

    assert expected == recieved


def test_proofs_can_save(migrated_pg_sync_session: Session):
    proof = Proofs(ref="proof-ref", description="proof descirption", clues=set())
    migrated_pg_sync_session.add(proof)
    migrated_pg_sync_session.commit()

    stmt = select(Proofs)
    recieved = migrated_pg_sync_session.execute(stmt).scalar()

    assert proof == recieved


def test_proofs_can_add_clues(migrated_pg_sync_session: Session):
    migrated_pg_sync_session.execute(
        text(
            """INSERT INTO proof(ref,description) VALUES('proof-ref','proof descirption')"""
        )
    )
    [[proof_id]] = migrated_pg_sync_session.execute(text("""SELECT id FROM proof"""))
    migrated_pg_sync_session.execute(
        text(
            """INSERT INTO clue(ref,description) VALUES
            ('ref-1','clue description')"""
        )
    )
    [[clue_id]] = migrated_pg_sync_session.execute(text("""SELECT id FROM clue"""))
    migrated_pg_sync_session.execute(
        text(
            f"""INSERT INTO proof_clue(proof_id,clue_id) VALUES({proof_id},{clue_id})"""
        )
    )
    stmt = select(Proofs)
    expected = Proofs(
        ref="proof-ref",
        description="proof descirption",
        clues={Clue(ref="ref-1", description="clue description")},
    )
    recieved = migrated_pg_sync_session.execute(stmt).scalar()
    assert expected == recieved
