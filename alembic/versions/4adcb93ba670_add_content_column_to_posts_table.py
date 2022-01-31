"""add_content_column_to_posts_table

Revision ID: 4adcb93ba670
Revises: 2e1155346251
Create Date: 2022-01-08 16:24:05.856162

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4adcb93ba670'
down_revision = '2e1155346251'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
