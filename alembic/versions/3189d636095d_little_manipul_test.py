"""little_manipul_test

Revision ID: 3189d636095d
Revises: 4a86bf989232
Create Date: 2022-01-08 17:04:15.965908

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3189d636095d'
down_revision = '4a86bf989232'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('nickname', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'nickname')
    # ### end Alembic commands ###
