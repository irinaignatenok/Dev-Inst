"""empty message

Revision ID: 79043ee6c5f6
Revises: 69052e3a9fd4
Create Date: 2020-08-19 08:24:54.057235

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79043ee6c5f6'
down_revision = '69052e3a9fd4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('class',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('class_name', sa.String(length=264), nullable=True),
    sa.Column('max_capacity', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('students_in_class',
    sa.Column('class_id', sa.Integer(), nullable=True),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['class_id'], ['class.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['user.id'], )
    )
    op.add_column('user', sa.Column('class_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'user', 'class', ['class_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_column('user', 'class_id')
    op.drop_table('students_in_class')
    op.drop_table('class')
    # ### end Alembic commands ###
