from sqlalchemy import text, select
from sqlalchemy.orm import Session
from app.domain.criminal import Criminal
from app.domain.criminal.criminal_type import CriminalType
from app.tests.integration.test_orm.conftest import (
    insert_characteristics,
    insert_dossier,
)
from app.domain.person import Person
from app.domain.person.characteristics import Characteristics, sex, color
from app.domain.person.dossier import Dossier
from app.domain.person.dossier.status.marrige_status import MarriageStatus
from app.domain.person.dossier.status.social_status import SocialStatus


def insert_criminal(criminal_type: str, session: Session):
    insert_characteristics(
        "characteristics-ref",
        12.3,
        10.3,
        10,
        "MALE",
        "blue",
        "brown",
        "chinese",
        session,
    )
    [[characteristics_id]] = session.execute(text("SELECT id FROM characteristics"))

    insert_dossier(
        "dossier-ref",
        "some history text 1",
        "WORKS",
        "MARRIED",
        session,
    )
    [[dossier_id]] = session.execute(text("SELECT id FROM dossier"))

    session.execute(
        text(
            f"""INSERT INTO person(ref,characteristics_id,dossier_id)
            VALUES('person-ref',{characteristics_id},{dossier_id})"""
        )
    )
    [[person_id]] = session.execute(text("SELECT id FROM person"))

    session.execute(
        text(
            f"""INSERT INTO criminal(person_id,criminal_type) VALUES({person_id},'{criminal_type}')"""
        )
    )


def make_criminal() -> Criminal:
    characteristics = Characteristics(
        ref="characteristics-ref",
        weight=12.3,
        height=10.3,
        age=10,
        sex=sex.Sex.MALE,
        _eyes_color=color.Color.color_from_name("blue"),
        _hairs_color=color.Color.color_from_name("brown"),
        nationality="chinese",
        special_signs=set(),
    )

    dossier = Dossier(
        "dossier-ref",
        "some history text 1",
        set(),
        set(),
        SocialStatus.WORKS,
        MarriageStatus.MARRIED,
    )

    person = Person(
        ref="person-ref",
        characteristics=characteristics,
        dossier=dossier,
    )
    return Criminal(person, CriminalType.DISMANTLER)


def test_criminal_can_read(migrated_pg_sync_session: Session):
    insert_criminal(CriminalType.DISMANTLER, migrated_pg_sync_session)
    expected = make_criminal()
    stmt = select(Criminal)
    recieved = migrated_pg_sync_session.execute(stmt).scalar()
    assert expected == recieved


def test_criminal_can_save(migrated_pg_sync_session: Session):
    criminal = make_criminal()
    migrated_pg_sync_session.add(criminal)
    migrated_pg_sync_session.commit()
    stmt = select(Criminal)
    recieved = migrated_pg_sync_session.execute(stmt).scalar()
    assert criminal == recieved
