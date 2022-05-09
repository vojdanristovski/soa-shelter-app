"""create dog table3

Revision ID: 9e02c33a6988
Revises: db882ccbd9e3
Create Date: 2022-05-09 22:08:54.402259

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '9e02c33a6988'
down_revision = 'db882ccbd9e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dogs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_url', sa.String(length=255), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('is_chipped', sa.Boolean(), nullable=True),
    sa.Column('coordinates', sa.String(length=255), nullable=True),
    sa.Column('breed', postgresql.ENUM('MALTESE', 'CORGI', 'POODLE', 'PUG', 'BICHON', 'POMERANIAN', 'BOXER', name='breeds'), nullable=False),
    sa.Column('dog_status', postgresql.ENUM('LOST', 'WAITING', 'SHELTERED', 'RESERVED', 'RESCUED', name='statuses'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dogs')
    # ### end Alembic commands ###
