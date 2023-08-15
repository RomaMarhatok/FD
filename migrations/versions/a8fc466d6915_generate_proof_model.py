"""generate proof model

Revision ID: a8fc466d6915
Revises: 198d71d80066
Create Date: 2023-08-15 14:28:23.767834

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8fc466d6915'
down_revision = '198d71d80066'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('proof',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ref', sa.String(length=255), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('ref')
    )
    op.create_table('proof_clue',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('proof_id', sa.Integer(), nullable=False),
    sa.Column('clue_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['clue_id'], ['clue.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['proof_id'], ['proof.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('proof_clue')
    op.drop_table('proof')
    # ### end Alembic commands ###
