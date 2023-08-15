from sqlalchemy import Table, Column, Integer, String, ForeignKey, Enum
from app.db.models.base import SqlAlchemyBaseModel
from app.domain.detective_history.status import PersonStatusInDetectiveHistory

detective_history_table = Table(
    "detective_history",
    SqlAlchemyBaseModel.metadata,
    Column("id", Integer(), primary_key=True),
    Column("ref", String(255), unique=True, nullable=False),
    Column("incident_description", String(255), nullable=False),
    Column("answer", ForeignKey("person.id", ondelete="SET NULL"), nullable=True),
)

detective_history_clue_table = Table(
    "detective_history_clue",
    SqlAlchemyBaseModel.metadata,
    Column("id", Integer(), primary_key=True),
    Column(
        "detective_history_id",
        ForeignKey("detective_history.id", ondelete="CASCADE"),
        nullable=False,
    ),
    Column(
        "clue_id",
        ForeignKey("clue.id", ondelete="CASCADE"),
        nullable=False,
    ),
)
detective_history_proofs_table = Table(
    "detective_history_proof",
    SqlAlchemyBaseModel.metadata,
    Column("id", Integer(), primary_key=True),
    Column(
        "detective_history_id",
        ForeignKey("detective_history.id", ondelete="CASCADE"),
        nullable=False,
    ),
    Column(
        "proof_id",
        ForeignKey("proof.id", ondelete="CASCADE"),
        nullable=False,
    ),
)

detective_history_member_table = Table(
    "history_member",
    SqlAlchemyBaseModel.metadata,
    Column("id", Integer(), primary_key=True),
    Column(
        "detective_history_id",
        ForeignKey("detective_history.id", ondelete="CASCADE"),
        nullable=False,
    ),
    Column("person_id", ForeignKey("person.id", ondelete="CASCADE"), nullable=False),
    Column(
        "person_status",
        Enum(PersonStatusInDetectiveHistory),
        nullable=False,
    ),
)
