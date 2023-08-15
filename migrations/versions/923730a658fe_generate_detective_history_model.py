"""generate detective history model

Revision ID: 923730a658fe
Revises: 682b35f709ce
Create Date: 2023-08-15 17:56:04.086644

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "923730a658fe"
down_revision = "682b35f709ce"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "detective_history",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("ref", sa.String(length=255), nullable=False),
        sa.Column("incident_description", sa.String(length=255), nullable=False),
        sa.Column("answer", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["answer"], ["person.id"], ondelete="SET NULL"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("ref"),
    )
    op.create_table(
        "detective_history_clue",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("detective_history_id", sa.Integer(), nullable=False),
        sa.Column("clue_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["clue_id"], ["clue.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(
            ["detective_history_id"], ["detective_history.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "detective_history_proof",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("detective_history_id", sa.Integer(), nullable=False),
        sa.Column("proof_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["detective_history_id"], ["detective_history.id"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(["proof_id"], ["proof.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "history_member",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("detective_history_id", sa.Integer(), nullable=False),
        sa.Column("person_id", sa.Integer(), nullable=False),
        sa.Column(
            "person_status",
            sa.Enum(
                "SUSPECT",
                "WITNESS",
                "CRIMINAL",
                "INNOCENT",
                "GUILTY",
                name="personstatusindetectivehistory",
            ),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["detective_history_id"], ["detective_history.id"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(["person_id"], ["person.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("history_member")
    op.drop_table("detective_history_proof")
    op.drop_table("detective_history_clue")
    op.drop_table("detective_history")
    sa.Enum(
        "SUSPECT",
        "WITNESS",
        "CRIMINAL",
        "INNOCENT",
        "GUILTY",
        name="personstatusindetectivehistory",
    ).drop(op.get_bind(), checkfirst=True)
    # ### end Alembic commands ###
