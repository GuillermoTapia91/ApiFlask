"""cree tabla areas

Revision ID: 8335609f827a
Revises: 
Create Date: 2023-05-27 15:59:39.986319

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8335609f827a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Areas',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.Text(), nullable=False),
    sa.Column('piso', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Areas')
    # ### end Alembic commands ###
