"""empty message

Revision ID: f6110ac9b9ca
Revises: 
Create Date: 2020-01-16 09:59:20.163764

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f6110ac9b9ca'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('actor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('movie',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('association',
    sa.Column('actor_id', sa.Integer(), nullable=True),
    sa.Column('movie_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['actor_id'], ['actor.id'], ),
    sa.ForeignKeyConstraint(['movie_id'], ['movie.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('association')
    op.drop_table('movie')
    op.drop_table('actor')
    # ### end Alembic commands ###