from sqlalchemy.ext.asyncio import AsyncSession
from .abstract_uow import AbstractUnitOfWork
from app.db.repositories.base.abstract_repo import AbstractRepository


class SqlAlchemyUnitOfWork(AbstractUnitOfWork):
    def __init__(
        self,
        session: AsyncSession,
        repo: AbstractRepository,
    ) -> None:
        self.session = session
        self.repo = repo

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await super().__aexit__(exc_type, exc_value, traceback)
        await self.session.close()

    async def commit(self):
        return await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
