from sqlalchemy import Table, Column, Text, Integer, Enum, ForeignKey, String
from app.db.models.base import SqlAlchemyBaseModel
from app.domain.person.dossier.status.marrige_status import MarriageStatus
from app.domain.person.dossier.status.social_status import SocialStatus

dossier_table = Table(
    "dossier",
    SqlAlchemyBaseModel.metadata,
    Column("id", Integer(), primary_key=True),
    Column("ref", String(255), nullable=False, unique=True, index=True),
    Column("history", Text(), nullable=False),
    Column("social_status", Enum(SocialStatus), nullable=False),
    Column("marriage_status", Enum(MarriageStatus), nullable=False),
)

dossier_hobbies_table = Table(
    "dossier_hobby",
    SqlAlchemyBaseModel.metadata,
    Column("id", Integer(), primary_key=True),
    Column("dossier_id", ForeignKey("dossier.id", ondelete="CASCADE"), nullable=False),
    Column("hobby_id", ForeignKey("hobby.id", ondelete="SET NULL"), nullable=False),
)

dossier_motives_table = Table(
    "dossier_motive",
    SqlAlchemyBaseModel.metadata,
    Column("id", Integer(), primary_key=True),
    Column("dossier_id", ForeignKey("dossier.id", ondelete="CASCADE"), nullable=False),
    Column("motive_id", ForeignKey("motive.id", ondelete="SET NULL"), nullable=False),
)
