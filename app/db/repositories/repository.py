from typing import Generic, TypeVar
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.repositories.base.abstract_repo import AbstractRepository

DOMAIN_MODEL = TypeVar("DOMAIN_MODEL")


class SqlAlchemyRepository(Generic[DOMAIN_MODEL], AbstractRepository):
    def __init__(self, session: AsyncSession, model: DOMAIN_MODEL) -> None:
        self.session = session
        self.model = model

    async def get(self, reference: str) -> DOMAIN_MODEL:
        stmt = select(self.model).filter_by(ref=reference)
        return (await self.session.execute(stmt)).scalar()

    async def add(self, instance: DOMAIN_MODEL) -> None:
        self.session.add(instance)

    async def list(self) -> list[DOMAIN_MODEL]:
        stmt = select(self.model)
        return (await self.session.execute(stmt)).scalars()
