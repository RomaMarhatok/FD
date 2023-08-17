import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.repositories.repository import SqlAlchemyRepository
from app.db.uow.base_uow import SqlAlchemyUnitOfWork
from app.domain.person import Person
from app.domain.detective_history.clue import Clue
from app.tests.integration.test_uow.conftest import make_person


@pytest.mark.asyncio
async def test_uow_can_save(migrated_pg_async_session: AsyncSession):
    person = await make_person()
    repo = SqlAlchemyRepository[Person](migrated_pg_async_session, Person)
    uow = SqlAlchemyUnitOfWork(migrated_pg_async_session, repo)
    async with uow:
        await uow.repo.add(person)
        await uow.commit()
        received = await uow.repo.get(person.ref)
        assert person == received


@pytest.mark.asyncio
async def test_uow_can_read(migrated_pg_async_session: AsyncSession):
    await migrated_pg_async_session.execute(
        text("""INSERT INTO clue(ref,description) VALUES('ref','description')""")
    )
    repo = SqlAlchemyRepository[Clue](migrated_pg_async_session, Clue)
    uow = SqlAlchemyUnitOfWork(migrated_pg_async_session, repo)
    expected = Clue(ref="ref", description="description")
    received = await uow.repo.get("ref")
    assert expected == received
