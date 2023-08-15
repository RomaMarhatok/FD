from sqlalchemy import Table, Column, String, Integer, ForeignKey
from app.db.models.base import SqlAlchemyBaseModel
from app.db.models.person.characteristics import characteristics_table
from app.db.models.person.dossier import dossier_table


person_table = Table(
    "person",
    SqlAlchemyBaseModel.metadata,
    Column("id", Integer(), primary_key=True),
    Column("ref", String(255), unique=True, nullable=False),
    Column(
        "characteristics_id",
        ForeignKey("characteristics.id", ondelete="SET NULL"),
        nullable=True,
    ),
    Column(
        "dossier_id",
        ForeignKey("dossier.id", ondelete="SET NULL"),
        nullable=True,
    ),
)
