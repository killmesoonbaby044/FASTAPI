"""nickname nullable

Revision ID: e0dae74d8d2a
Revises: 3189d636095d
Create Date: 2022-01-08 17:08:18.765473

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0dae74d8d2a'
down_revision = '3189d636095d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'nickname',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'nickname',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
