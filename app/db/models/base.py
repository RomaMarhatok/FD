from sqlalchemy import MetaData, orm


class SqlAlchemyModel(orm.DeclarativeBase):
    metadata = MetaData()
