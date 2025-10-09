"""Create posts table

Revision ID: 5fb6e16a0e91
Revises: 
Create Date: 2025-10-09 15:37:58.934811

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5fb6e16a0e91'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts',sa.column('id',sa.Integer(), nulllabe=False, primary_key=True), sa.column('title',sa.string(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
