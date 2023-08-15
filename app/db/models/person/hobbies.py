from sqlalchemy import Table, Column, String, Text, Integer
from app.db.models.base import SqlAlchemyBaseModel

hobbies_table = Table(
    "hobby",
    SqlAlchemyBaseModel.metadata,
    Column("id", Integer(), primary_key=True),
    Column("ref", String(255), nullable=False, unique=True, index=True),
    Column("description", Text(), nullable=False),
)
