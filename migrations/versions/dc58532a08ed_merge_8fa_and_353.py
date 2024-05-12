"""merge 8fa and 353

Revision ID: dc58532a08ed
Revises: 353f504302ed, 8fafa7833a77
Create Date: 2024-05-08 15:39:51.466779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc58532a08ed'
down_revision = ('353f504302ed', '8fafa7833a77')
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
