"""empty message

Revision ID: 2b7d8cae7535
Revises: c46246e283a4
Create Date: 2023-11-26 09:51:37.191552

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b7d8cae7535'
down_revision = 'c46246e283a4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('uq__payment_method__method_id', 'payment_method', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('uq__payment_method__method_id', 'payment_method', ['method_id'])
    # ### end Alembic commands ###
