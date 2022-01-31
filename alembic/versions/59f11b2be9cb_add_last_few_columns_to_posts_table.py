"""add_last_few_columns_to_posts_table

Revision ID: 59f11b2be9cb
Revises: ccbab3c62123
Create Date: 2022-01-08 16:28:12.608595

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59f11b2be9cb'
down_revision = 'ccbab3c62123'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass

