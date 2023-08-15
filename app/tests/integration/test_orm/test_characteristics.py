from sqlalchemy import text, select
from sqlalchemy.orm import Session
from app.domain.person.characteristics import Characteristics, color, sex, special_sign
from app.tests.integration.test_orm.conftest import insert_characteristics


def test_characteristics_can_read(migrated_pg_sync_session: Session):
    insert_characteristics(
        "ref-1",
        12.3,
        10.3,
        10,
        "MALE",
        "blue",
        "brown",
        "chinese",
        migrated_pg_sync_session,
    )
    stmt = select(Characteristics)
    received = migrated_pg_sync_session.execute(stmt).scalar()
    expected = Characteristics(
        ref="ref-1",
        weight=12.3,
        height=10.3,
        age=10,
        sex=sex.Sex.MALE,
        _eyes_color=color.Color.color_from_name("blue"),
        _hairs_color=color.Color.color_from_name("brown"),
        nationality="chinese",
        special_signs=set(),
    )
    assert received == expected


def test_characteristics_can_save(migrated_pg_sync_session: Session):
    characteristics = Characteristics(
        ref="ref-1",
        weight=12.3,
        height=10.3,
        age=10,
        sex=sex.Sex.MALE,
        _eyes_color=color.Color.color_from_name("gray"),
        _hairs_color=color.Color.color_from_name("purple"),
        nationality="nationality-1",
        special_signs=set(),
    )
    migrated_pg_sync_session.add(characteristics)
    migrated_pg_sync_session.commit()
    stmt = select(Characteristics).where(Characteristics.ref == characteristics.ref)
    received = migrated_pg_sync_session.execute(stmt).scalar()
    assert characteristics == received


def test_characteristics_can_add_special_sign(migrated_pg_sync_session: Session):
    characteristics = Characteristics(
        ref="ref-1",
        weight=12.3,
        height=10.3,
        age=10,
        sex=sex.Sex.MALE,
        _eyes_color=color.Color.color_from_name("gray"),
        _hairs_color=color.Color.color_from_name("purple"),
        nationality="nationality-1",
        special_signs=set(),
    )
    sign = special_sign.SpecialSign(ref="ref-1", description="desc-1")
    characteristics.special_signs.add(sign)
    migrated_pg_sync_session.add(characteristics)
    migrated_pg_sync_session.commit()
    stmt = select(Characteristics).where(Characteristics.ref == characteristics.ref)
    recieved = migrated_pg_sync_session.execute(stmt).scalar()
    assert characteristics == recieved


def test_characteristics_retrieving_special_signs(migrated_pg_sync_session: Session):
    migrated_pg_sync_session.execute(
        text("INSERT INTO special_sign(ref,description) VALUES ('ref-1','desc-1')")
    )
    [[sid]] = migrated_pg_sync_session.execute(text("SELECT id FROM special_sign"))
    insert_characteristics(
        "ref-1",
        12.3,
        10.3,
        10,
        "MALE",
        "yellow",
        "white",
        "european",
        migrated_pg_sync_session,
    )
    [[cid]] = migrated_pg_sync_session.execute(text("SELECT id FROM characteristics"))
    migrated_pg_sync_session.execute(
        text(
            f"INSERT INTO special_sign_in_characteristics(characteristic_id,special_sign_id) VALUES({cid},{sid})"
        )
    )
    stmt = select(Characteristics)
    characteristics = migrated_pg_sync_session.execute(stmt).scalar()
    assert characteristics.special_signs == {
        special_sign.SpecialSign(ref="ref-1", description="desc-1")
    }
