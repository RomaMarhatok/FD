from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase


class SqlAlchemyBaseModel(DeclarativeBase):
    metadata = MetaData()
