"""generate special sign model

Revision ID: 61d733c0f020
Revises: 
Create Date: 2023-08-13 19:23:37.907340

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "61d733c0f020"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "special_sign",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("ref", sa.String(length=255), nullable=True),
        sa.Column("description", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("ref"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("special_sign")
    # ### end Alembic commands ###
