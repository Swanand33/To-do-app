"""Create tasks table

Revision ID: c307e34c91a2
Revises: 
Create Date: 2024-06-28 20:49:00.358102

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c307e34c91a2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('task',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('category', sa.String(length=50), nullable=False),
    sa.Column('priority', sa.String(length=50), nullable=False),
    sa.Column('due_date', sa.DateTime(), nullable=True),
    sa.Column('completed', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('task')
    # ### end Alembic commands ###
