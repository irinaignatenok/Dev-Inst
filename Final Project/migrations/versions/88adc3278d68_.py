"""empty message

Revision ID: 88adc3278d68
Revises: 79043ee6c5f6
Create Date: 2020-08-19 12:18:01.065182

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88adc3278d68'
down_revision = '79043ee6c5f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('students_in_class')
    op.drop_constraint(None, 'class', type_='foreignkey')
    op.drop_column('class', 'user_id')
    op.create_foreign_key(None, 'user', 'class', ['class_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.add_column('class', sa.Column('user_id', sa.INTEGER(), nullable=True))
    op.create_foreign_key(None, 'class', 'user', ['user_id'], ['id'])
    op.create_table('students_in_class',
    sa.Column('class_id', sa.INTEGER(), nullable=True),
    sa.Column('student_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['class_id'], ['class.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['user.id'], )
    )
    # ### end Alembic commands ###
