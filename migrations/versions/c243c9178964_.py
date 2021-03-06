"""empty message

Revision ID: c243c9178964
Revises: 
Create Date: 2019-09-22 19:18:36.091048

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c243c9178964'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=180), nullable=True),
    sa.Column('email', sa.String(length=180), nullable=True),
    sa.Column('password', sa.String(length=180), nullable=True),
    sa.Column('cellphone', sa.String(length=180), nullable=True),
    sa.Column('photo', sa.String(length=180), nullable=True),
    sa.Column('roles', sa.JSON(), nullable=True),
    sa.Column('deleted', sa.Boolean(), nullable=True),
    sa.Column('blocked', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
