from sqlalchemy import Table, Column, String, Integer, Text
from app.db.models.base import SqlAlchemyBaseModel

clue_table = Table(
    "clue",
    SqlAlchemyBaseModel.metadata,
    Column("id", Integer(), primary_key=True),
    Column("ref", String(255), unique=True, nullable=False),
    Column("description", Text(), nullable=False),
)
