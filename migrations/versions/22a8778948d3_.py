"""empty message

Revision ID: 22a8778948d3
Revises: dda8ac02bfa2
Create Date: 2019-09-24 23:45:20.545939

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22a8778948d3'
down_revision = 'dda8ac02bfa2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=180), nullable=True),
    sa.Column('email', sa.String(length=180), nullable=True),
    sa.Column('cellphone', sa.String(length=180), nullable=True),
    sa.Column('photo', sa.String(length=180), nullable=True),
    sa.Column('classes_per_week', sa.Integer(), nullable=True),
    sa.Column('weeks', sa.Integer(), nullable=True),
    sa.Column('level', sa.String(length=180), nullable=True),
    sa.Column('monthly_payment', sa.Integer(), nullable=True),
    sa.Column('message', sa.String(length=6000), nullable=True),
    sa.Column('deleted', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('student')
    # ### end Alembic commands ###
