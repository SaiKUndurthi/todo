"""empty message

Revision ID: 67019b8e0def
Revises: 5865cb0772c0
Create Date: 2020-05-24 16:12:16.428153

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67019b8e0def'
down_revision = '5865cb0772c0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('completed', sa.Boolean(), nullable=True))

    op.execute('UPDATE todos SET completed = False WHERE completed is NULL')
    # ### end Alembic commands ###

    op.alter_column('todos', 'completed', nullable=False)


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todos', 'completed')
    # ### end Alembic commands ###
