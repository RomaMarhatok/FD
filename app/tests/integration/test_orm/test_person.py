from sqlalchemy import text, select
from sqlalchemy.orm import Session
from app.domain.person import Person
from app.domain.person.characteristics import Characteristics, sex, color
from app.domain.person.dossier import Dossier
from app.domain.person.dossier.status.marrige_status import MarriageStatus
from app.domain.person.dossier.status.social_status import SocialStatus
from app.tests.integration.test_orm.conftest import (
    insert_characteristics,
    insert_dossier,
)


def test_person_can_read(migrated_pg_sync_session: Session):
    insert_characteristics(
        "characteristics-ref",
        12.3,
        10.3,
        10,
        "MALE",
        "blue",
        "brown",
        "chinese",
        migrated_pg_sync_session,
    )

    [[characteristics_id]] = migrated_pg_sync_session.execute(
        text("SELECT id FROM characteristics")
    )
    insert_dossier(
        "dossier-ref",
        "some history text 1",
        "WORKS",
        "MARRIED",
        migrated_pg_sync_session,
    )
    [[dossier_id]] = migrated_pg_sync_session.execute(text("SELECT id FROM dossier"))
    migrated_pg_sync_session.execute(
        text(
            f"""INSERT INTO person(ref,characteristics_id,dossier_id)
            VALUES('person-ref',{characteristics_id},{dossier_id})"""
        )
    )
    stmt = select(Person)
    received = migrated_pg_sync_session.execute(stmt).scalar()
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

    expected = Person(
        ref="person-ref",
        characteristics=characteristics,
        dossier=dossier,
    )
    assert received == expected


def test_person_can_save(migrated_pg_sync_session: Session):
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
    migrated_pg_sync_session.add(person)
    migrated_pg_sync_session.commit()
    stmt = select(Person)
    received = migrated_pg_sync_session.execute(stmt).scalar()
    assert person == received
