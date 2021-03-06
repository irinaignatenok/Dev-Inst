"""empty message

Revision ID: afd035973f83
Revises: c4b13158f220
Create Date: 2020-07-16 19:56:57.932168

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'afd035973f83'
down_revision = 'c4b13158f220'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todo_list', sa.Column('is_complete', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todo_list', 'is_complete')
    # ### end Alembic commands ###
