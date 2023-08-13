import uuid
from sqlalchemy import text, select
from sqlalchemy.orm import Session
from app.domain.person.characteristics.special_sign import SpecialSign


def test_special_sign_mapper_can_read(migrated_pg_sync_session: Session):
    sql = text(
        "INSERT INTO special_sign(ref,description) VALUES ('ref-1','desc-1'),('ref-2','desc-2'),('ref-3','desc-3')"
    )
    migrated_pg_sync_session.execute(sql)
    expected = [
        SpecialSign(ref="ref-1", description="desc-1"),
        SpecialSign(ref="ref-2", description="desc-2"),
        SpecialSign(ref="ref-3", description="desc-3"),
    ]
    received = migrated_pg_sync_session.execute(select(SpecialSign)).scalars().all()
    assert received == expected


def test_special_sign_can_add(migrated_pg_sync_session: Session):
    expected = SpecialSign(ref="ref-1", description="desc-1")
    migrated_pg_sync_session.add(expected)
    migrated_pg_sync_session.commit()
    stmt = select(SpecialSign).where(SpecialSign.ref == expected.ref)
    recieved = migrated_pg_sync_session.execute(stmt).scalar()
    assert expected == recieved
