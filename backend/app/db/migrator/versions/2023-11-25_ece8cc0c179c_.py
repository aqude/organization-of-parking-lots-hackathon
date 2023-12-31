"""empty message

Revision ID: ece8cc0c179c
Revises: 9fe236385356
Create Date: 2023-11-25 18:47:15.848022

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ece8cc0c179c'
down_revision = '9fe236385356'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Places', sa.Column('price', sa.DECIMAL(), nullable=False))
    op.drop_column('Places', 'price_for_hour')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Places', sa.Column('price_for_hour', sa.NUMERIC(), autoincrement=False, nullable=False))
    op.drop_column('Places', 'price')
    # ### end Alembic commands ###
