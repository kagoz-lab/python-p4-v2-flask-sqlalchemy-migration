"""Rename address to location

Revision ID: 663965c80a1c
Revises: 94e9f2b7064b
Create Date: 2025-04-08 21:25:51.369905

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '663965c80a1c'
down_revision = '94e9f2b7064b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'address', new_column_name='location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'location', new_column_name='address')
    # ### end Alembic commands ###
