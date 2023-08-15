from sqlalchemy import select, text
from sqlalchemy.orm import Session
from app.domain.detective_history import DetectiveHistory
from app.domain.detective_history.clue import Clue
from app.domain.detective_history.proofs import Proofs
from app.domain.detective_history.member import DetectiveHistoryMember
from app.tests.integration.test_orm.conftest import insert_person
from app.tests.integration.test_orm.test_person import make_person


def insert_detective_history(session: Session):
    insert_person(session)
    [[person_id]] = session.execute(text("""SELECT id FROM person"""))
    session.execute(
        text(
            f"""INSERT INTO detective_history(ref,incident_description,answer)
            VALUES('detective_history_ref','incident description',{person_id})"""
        )
    )
    [[detective_history_id]] = session.execute(
        text("""SELECT id FROM detective_history""")
    )
    session.execute(
        text(
            """INSERT INTO proof(ref,description) VALUES('proof-ref','proof descirption')"""
        )
    )
    [[proof_id]] = session.execute(text("""SELECT id FROM proof"""))
    session.execute(
        text(
            """INSERT INTO clue(ref,description) VALUES
            ('ref-1','clue description')"""
        )
    )
    [[clue_id]] = session.execute(text("""SELECT id FROM clue"""))
    session.execute(
        text(
            f"""INSERT INTO proof_clue(proof_id,clue_id) VALUES({proof_id},{clue_id})"""
        )
    )
    session.execute(
        text(
            f"""INSERT INTO detective_history_clue(detective_history_id,clue_id)
            VALUES({detective_history_id},{clue_id})"""
        )
    )
    session.execute(
        text(
            f"""INSERT INTO detective_history_proof(detective_history_id,proof_id)
            VALUES({detective_history_id},{proof_id})"""
        )
    )
    session.execute(
        text(
            f"""INSERT INTO history_member(detective_history_id,person_id,person_status)
            VALUES({detective_history_id},{person_id},'INNOCENT')"""
        )
    )


def make_detective_history() -> DetectiveHistory:
    clue = Clue(ref="ref-1", description="clue description")
    proof = Proofs(ref="proof-ref", description="proof descirption", clues={clue})
    person = make_person()
    member = DetectiveHistoryMember(person=person)
    return DetectiveHistory(
        ref="detective_history_ref",
        incident_description="incident description",
        clues={clue},
        proofs={proof},
        members={member},
        history_answer=person,
    )


def test_detective_history_can_read(migrated_pg_sync_session: Session):
    insert_detective_history(migrated_pg_sync_session)
    stmt = select(DetectiveHistory)
    recieved = migrated_pg_sync_session.execute(stmt).scalar()
    expected = make_detective_history()
    assert recieved == expected


def test_detective_history_can_save(migrated_pg_sync_session: Session):
    detective_history = make_detective_history()
    migrated_pg_sync_session.add(detective_history)
    migrated_pg_sync_session.commit()
    stmt = select(DetectiveHistory)
    recieved = migrated_pg_sync_session.execute(stmt).scalar()
    assert detective_history == recieved
