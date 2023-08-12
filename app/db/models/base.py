from sqlalchemy import MetaData, orm
from sqlalchemy.orm import registry

mapper_registry = registry()


class SqlAlchemyModel(orm.DeclarativeBase):
    metadata = MetaData()
