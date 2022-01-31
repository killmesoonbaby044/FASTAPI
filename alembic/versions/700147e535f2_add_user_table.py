"""add_user_table

Revision ID: 700147e535f2
Revises: 4adcb93ba670
Create Date: 2022-01-08 16:25:12.719789

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '700147e535f2'
down_revision = '4adcb93ba670'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass

