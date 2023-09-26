"""empty message

Revision ID: c568c3b1abee
Revises: 64e4073d5228
Create Date: 2023-09-25 21:39:52.846587

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c568c3b1abee'
down_revision = '64e4073d5228'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.drop_column('birthday')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.add_column(sa.Column('birthday', sa.DATETIME(), nullable=True))

    # ### end Alembic commands ###
