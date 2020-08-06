"""empty message

Revision ID: 72a646a6fe67
Revises: 
Create Date: 2020-08-03 14:44:04.211547

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72a646a6fe67'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=264), nullable=True),
    sa.Column('username', sa.String(length=264), nullable=True),
    sa.Column('email', sa.String(length=264), nullable=True),
    sa.Column('password', sa.String(length=264), nullable=True),
    sa.Column('role', sa.String(length=264), nullable=True),
    sa.Column('test', sa.String(length=264), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
