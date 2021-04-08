"""add back foto

Revision ID: 1e476d25c36c
Revises: 06a6b14e4591
Create Date: 2021-03-31 17:22:01.809393

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e476d25c36c'
down_revision = '06a6b14e4591'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('masalah', sa.Column('foto', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('masalah', 'foto')
    # ### end Alembic commands ###
