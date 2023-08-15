from sqlalchemy import Table, Column, Integer, ForeignKey, Enum
from app.db.models.base import SqlAlchemyBaseModel
from app.domain.criminal.criminal_type import CriminalType

criminal_table = Table(
    "criminal",
    SqlAlchemyBaseModel.metadata,
    Column("id", Integer(), primary_key=True),
    Column("person_id", ForeignKey("person.id", ondelete="CASCADE"), nullable=False),
    Column("criminal_type", Enum(CriminalType), nullable=False),
)
