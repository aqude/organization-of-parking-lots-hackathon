"""empty message

Revision ID: 771109004d83
Revises: 2e338a5d71a7
Create Date: 2023-11-25 01:53:02.360063

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '771109004d83'
down_revision = '2e338a5d71a7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reservations',
    sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('gen_random_uuid()'), nullable=False),
    sa.Column('dt_created', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('dt_updated', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('place_id', sa.INTEGER(), nullable=False),
    sa.Column('occupied_from', sa.TIMESTAMP(), nullable=False),
    sa.Column('occupied_to', sa.TIMESTAMP(), nullable=False),
    sa.Column('payment_method_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('payment_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.ForeignKeyConstraint(['payment_id'], ['payment.id'], name=op.f('fk__reservations__payment_id__payment'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['payment_method_id'], ['payment_method.id'], name=op.f('fk__reservations__payment_method_id__payment_method'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk__reservations__user_id__user'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__reservations')),
    sa.UniqueConstraint('id', name=op.f('uq__reservations__id')),
    sa.UniqueConstraint('place_id', name=op.f('uq__reservations__place_id')),
    sa.UniqueConstraint('user_id', name=op.f('uq__reservations__user_id'))
    )
    op.add_column('Places', sa.Column('status', sa.Boolean(), nullable=True))
    op.alter_column('Places', 'price_for_hour',
               existing_type=sa.INTEGER(),
               type_=sa.DECIMAL(),
               existing_nullable=False)
    op.drop_column('Places', 'time_occupied_from')
    op.drop_column('Places', 'time_occupied_to')
    op.create_unique_constraint(op.f('uq__payment__id'), 'payment', ['id'])
    op.create_unique_constraint(op.f('uq__payment_method__id'), 'payment_method', ['id'])
    op.create_unique_constraint(op.f('uq__user__id'), 'user', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('uq__user__id'), 'user', type_='unique')
    op.drop_constraint(op.f('uq__payment_method__id'), 'payment_method', type_='unique')
    op.drop_constraint(op.f('uq__payment__id'), 'payment', type_='unique')
    op.add_column('Places', sa.Column('time_occupied_to', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True))
    op.add_column('Places', sa.Column('time_occupied_from', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True))
    op.alter_column('Places', 'price_for_hour',
               existing_type=sa.DECIMAL(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    op.drop_column('Places', 'status')
    op.drop_table('reservations')
    # ### end Alembic commands ###
