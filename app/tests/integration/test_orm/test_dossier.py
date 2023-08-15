from sqlalchemy import select
from sqlalchemy.orm import Session
from app.domain.person.dossier import Dossier
from app.domain.person.dossier.status.marrige_status import MarriageStatus
from app.domain.person.dossier.status.social_status import SocialStatus
from app.domain.person.dossier.hobbies import Hobbies
from app.domain.person.dossier.motives import Motives
from app.tests.integration.test_orm.conftest import insert_dossier


def test_dossier_can_read(migrated_pg_sync_session: Session):
    insert_dossier(
        "ref-1", "some history text 1", "WORKS", "MARRIED", migrated_pg_sync_session
    )
    insert_dossier(
        "ref-2",
        "some history text 2",
        "UNEMPLOYED",
        "UNMARRIED",
        migrated_pg_sync_session,
    )
    insert_dossier(
        "ref-3", "some history text 3", "WORKS", "DIVORCED", migrated_pg_sync_session
    )
    expected = [
        Dossier(
            "ref-1",
            "some history text 1",
            set(),
            set(),
            SocialStatus.WORKS,
            MarriageStatus.MARRIED,
        ),
        Dossier(
            "ref-2",
            "some history text 2",
            set(),
            set(),
            SocialStatus.UNEMPLOYED,
            MarriageStatus.UNMARRIED,
        ),
        Dossier(
            "ref-3",
            "some history text 3",
            set(),
            set(),
            SocialStatus.WORKS,
            MarriageStatus.DIVORCED,
        ),
    ]
    stmt = select(Dossier)
    received = migrated_pg_sync_session.execute(stmt).scalars().all()
    assert expected == received


def test_dossier_can_save(migrated_pg_sync_session: Session):
    dossier = Dossier(
        "ref-1",
        "some history text 1",
        set(),
        set(),
        SocialStatus.WORKS,
        MarriageStatus.MARRIED,
    )
    migrated_pg_sync_session.add(dossier)
    migrated_pg_sync_session.commit()
    stmt = select(Dossier)
    received = migrated_pg_sync_session.execute(stmt).scalar()
    assert dossier == received


def test_dossier_can_add_hobby_and_motive(migrated_pg_sync_session: Session):
    dossier = Dossier(
        "ref-1",
        "some history text 1",
        set(),
        set(),
        SocialStatus.WORKS,
        MarriageStatus.MARRIED,
    )
    hobby = Hobbies(
        "ref-hobby",
        "hobby description",
    )
    motive = Motives(
        "ref-motive",
        "motive description",
    )
    dossier.hobbies.add(hobby)
    dossier.motives.add(motive)
    migrated_pg_sync_session.add(dossier)
    migrated_pg_sync_session.commit()
    stmt = select(Dossier)
    received = migrated_pg_sync_session.execute(stmt).scalar()
    assert received == dossier
