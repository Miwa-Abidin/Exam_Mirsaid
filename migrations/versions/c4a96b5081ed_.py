"""empty message

Revision ID: c4a96b5081ed
Revises: 
Create Date: 2022-12-01 13:37:21.214590

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4a96b5081ed'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password_hash', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('employee',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fullname', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('short_info', sa.String(), nullable=True),
    sa.Column('experience', sa.Integer(), nullable=True),
    sa.Column('preferred_position', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employee')
    op.drop_table('user')
    # ### end Alembic commands ###
