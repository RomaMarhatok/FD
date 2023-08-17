import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from app.tests.integration.test_repository.conftest import (
    make_person,
    make_detective_history,
)
from app.db.repositories.repository import SqlAlchemyRepository
from app.domain.person import Person
from app.domain.detective_history import DetectiveHistory
from app.domain.detective_history.clue import Clue


@pytest.mark.asyncio
async def test_repository_can_save_person(migrated_pg_async_session: AsyncSession):
    person = await make_person()
    repo = SqlAlchemyRepository[Person](migrated_pg_async_session, Person)
    await repo.add(person)
    await migrated_pg_async_session.commit()
    received = await repo.get(person.ref)
    assert received == person


@pytest.mark.asyncio
async def test_repository_can_read_person(migrated_pg_async_session: AsyncSession):
    expected = await make_person()
    migrated_pg_async_session.add(expected)
    await migrated_pg_async_session.commit()
    repo = SqlAlchemyRepository[Person](migrated_pg_async_session, Person)
    received = await repo.get(expected.ref)
    assert received == expected


@pytest.mark.asyncio
async def test_repository_can_save_detective_history(
    migrated_pg_async_session: AsyncSession,
):
    detective_history = await make_detective_history()
    repo = SqlAlchemyRepository[DetectiveHistory](
        migrated_pg_async_session, DetectiveHistory
    )
    await repo.add(detective_history)
    await migrated_pg_async_session.commit()
    received = await repo.get(detective_history.ref)
    assert detective_history == received


@pytest.mark.asyncio
async def test_repository_can_read_detective_history(
    migrated_pg_async_session: AsyncSession,
):
    detective_history = await make_detective_history()
    migrated_pg_async_session.add(detective_history)
    await migrated_pg_async_session.commit()
    repo = SqlAlchemyRepository[DetectiveHistory](
        migrated_pg_async_session, DetectiveHistory
    )
    received = await repo.get(detective_history.ref)
    assert detective_history == received


@pytest.mark.asyncio
async def test_repository_can_read_clue(migrated_pg_async_session: AsyncSession):
    clue = Clue(ref="clue-ref", description="descrition")
    migrated_pg_async_session.add(clue)
    await migrated_pg_async_session.commit()
    repo = SqlAlchemyRepository[Clue](migrated_pg_async_session, Clue)
    received = await repo.get(clue.ref)
    assert clue == received


@pytest.mark.asyncio
async def test_repository_can_save_clue(migrated_pg_async_session: AsyncSession):
    clue = Clue(ref="clue-ref", description="descrition")
    repo = SqlAlchemyRepository[Clue](migrated_pg_async_session, Clue)
    await repo.add(clue)
    await migrated_pg_async_session.commit()
    received = await repo.get(clue.ref)
    assert clue == received
