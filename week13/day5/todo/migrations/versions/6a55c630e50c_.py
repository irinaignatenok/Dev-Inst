"""empty message

Revision ID: 6a55c630e50c
Revises: afd035973f83
Create Date: 2020-07-17 10:19:41.938427

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a55c630e50c'
down_revision = 'afd035973f83'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todo_list', sa.Column('todo_id', sa.Integer(), nullable=False))
    op.drop_column('todo_list', 'id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todo_list', sa.Column('id', sa.INTEGER(), nullable=False))
    op.drop_column('todo_list', 'todo_id')
    # ### end Alembic commands ###