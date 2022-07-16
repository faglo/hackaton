"""empty message

Revision ID: 5654192dec37
Revises: 
Create Date: 2022-07-16 22:40:15.843030

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '5654192dec37'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('buildings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('residential_complex', sa.String(length=255), nullable=False),
    sa.Column('building', sa.String(length=10), nullable=False),
    sa.Column('entrance', sa.Integer(), nullable=False),
    sa.Column('floor', sa.Integer(), nullable=False),
    sa.Column('flat_num', sa.Integer(), nullable=False),
    sa.Column('area', sa.Integer(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=400), nullable=False),
    sa.Column('photo_links', postgresql.ARRAY(sa.String()), nullable=False),
    sa.Column('rooms', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_buildings_id'), 'buildings', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_buildings_id'), table_name='buildings')
    op.drop_table('buildings')
    # ### end Alembic commands ###