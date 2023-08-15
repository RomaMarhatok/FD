from app.db.models.base import SqlAlchemyBaseModel
from sqlalchemy import Column, Text, Table, Integer, String

special_sing_table = Table(
    "special_sign",
    SqlAlchemyBaseModel.metadata,
    Column("id", Integer(), primary_key=True),
    Column("ref", String(255), unique=True, nullable=True),
    Column("description", Text()),
)
