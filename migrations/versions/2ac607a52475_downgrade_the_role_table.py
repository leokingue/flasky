"""downgrade the Role table

Revision ID: 2ac607a52475
Revises: e402c18d3a8d
Create Date: 2023-09-13 23:03:34.176874

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ac607a52475'
down_revision = 'e402c18d3a8d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('roles', schema=None) as batch_op:
        batch_op.drop_index('ix_roles_default')
        batch_op.drop_column('permissions')
        batch_op.drop_column('default')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('roles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('default', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('permissions', sa.INTEGER(), nullable=True))
        batch_op.create_index('ix_roles_default', ['default'], unique=False)

    # ### end Alembic commands ###