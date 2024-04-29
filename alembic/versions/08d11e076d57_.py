"""empty message

Revision ID: 08d11e076d57
Revises: c5f87cd9a547, f1c57becd205
Create Date: 2024-04-29 22:17:22.546861

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '08d11e076d57'
down_revision: Union[str, None] = ('c5f87cd9a547', 'f1c57becd205')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
