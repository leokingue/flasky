"""update the Role table

Revision ID: e402c18d3a8d
Revises: 2899fbc8e3c4
Create Date: 2023-09-13 22:57:54.265847

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e402c18d3a8d'
down_revision = '2899fbc8e3c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('roles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('default', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('permissions', sa.Integer(), nullable=True))
        batch_op.create_index(batch_op.f('ix_roles_default'), ['default'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('roles', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_roles_default'))
        batch_op.drop_column('permissions')
        batch_op.drop_column('default')

    # ### end Alembic commands ###
