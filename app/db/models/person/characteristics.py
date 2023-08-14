from sqlalchemy import Table, Column, Integer, String, Float, Enum, ForeignKey
from app.db.models.base import SqlAlchemyBaseModel
from app.domain.person.characteristics.sex import Sex

characteristics_table = Table(
    "characteristics",
    SqlAlchemyBaseModel.metadata,
    Column("id", Integer(), primary_key=True),
    Column("ref", String(255), unique=True, nullable=True),
    Column("weight", Float(2), nullable=False),
    Column("height", Float(2), nullable=False),
    Column("age", Integer(), nullable=False),
    Column("sex", Enum(Sex), nullable=False),
    Column("eyes_color", String(255), nullable=False),
    Column("hairs_color", String(255), nullable=False),
    Column("nationality", String(255), nullable=False),
)

special_sign_in_characteristics_table = Table(
    "special_sign_in_characteristics",
    SqlAlchemyBaseModel.metadata,
    Column("id", Integer(), primary_key=True),
    Column(
        "characteristic_id",
        ForeignKey("characteristics.id", ondelete="CASCADE"),
        nullable=False,
    ),
    Column(
        "special_sign_id",
        ForeignKey("special_sign.id", ondelete="SET NULL"),
        nullable=True,
    ),
)
