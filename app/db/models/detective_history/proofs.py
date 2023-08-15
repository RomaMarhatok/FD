from sqlalchemy import Table, Column, String, Integer, Text, ForeignKey
from app.db.models.base import SqlAlchemyBaseModel

proof_table = Table(
    "proof",
    SqlAlchemyBaseModel.metadata,
    Column("id", Integer(), primary_key=True),
    Column("ref", String(255), unique=True, nullable=False),
    Column("description", Text(), nullable=False),
)

proof_clue_table = Table(
    "proof_clue",
    SqlAlchemyBaseModel.metadata,
    Column("id", Integer(), primary_key=True),
    Column("proof_id", ForeignKey("proof.id", ondelete="CASCADE"), nullable=False),
    Column("clue_id", ForeignKey("clue.id", ondelete="CASCADE"), nullable=False),
)
