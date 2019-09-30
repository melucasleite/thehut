"""empty message

Revision ID: 5aa0dd2a9586
Revises: 3000ef2e5e88
Create Date: 2019-09-30 10:51:23.508720

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5aa0dd2a9586'
down_revision = '3000ef2e5e88'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lecture_history_student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('present', sa.Boolean(), nullable=True),
    sa.Column('lecture_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('deleted', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['lecture_id'], ['lecture.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('remark_student', sa.Column('lecture_history_student_id', sa.Integer(), nullable=True))
    op.add_column('remark_student', sa.Column('positive', sa.Boolean(), nullable=True))
    op.drop_constraint(u'remark_student_ibfk_4', 'remark_student', type_='foreignkey')
    op.create_foreign_key(None, 'remark_student', 'lecture_history_student', ['lecture_history_student_id'], ['id'])
    op.drop_column('remark_student', 'student_lecture_history_id')
    op.add_column('skill_student', sa.Column('lecture_history_student_id', sa.Integer(), nullable=True))
    op.drop_constraint(u'skill_student_ibfk_4', 'skill_student', type_='foreignkey')
    op.create_foreign_key(None, 'skill_student', 'lecture_history_student', ['lecture_history_student_id'], ['id'])
    op.drop_column('skill_student', 'student_lecture_history_id')
    op.drop_table('student_lecture_history')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('skill_student', sa.Column('student_lecture_history_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'skill_student', type_='foreignkey')
    op.create_foreign_key(u'skill_student_ibfk_4', 'skill_student', 'student_lecture_history', ['student_lecture_history_id'], ['id'])
    op.drop_column('skill_student', 'lecture_history_student_id')
    op.add_column('remark_student', sa.Column('student_lecture_history_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'remark_student', type_='foreignkey')
    op.create_foreign_key(u'remark_student_ibfk_4', 'remark_student', 'student_lecture_history', ['student_lecture_history_id'], ['id'])
    op.drop_column('remark_student', 'positive')
    op.drop_column('remark_student', 'lecture_history_student_id')
    op.create_table('student_lecture_history',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('student_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('date', mysql.DATETIME(), nullable=True),
    sa.Column('lecture_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('deleted', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['lecture_id'], [u'lecture.id'], name=u'student_lecture_history_ibfk_1'),
    sa.ForeignKeyConstraint(['student_id'], [u'student.id'], name=u'student_lecture_history_ibfk_2'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.drop_table('lecture_history_student')
    # ### end Alembic commands ###
