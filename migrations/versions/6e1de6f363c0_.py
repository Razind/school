"""empty message

Revision ID: 6e1de6f363c0
Revises: 5e12ed2c8ffb
Create Date: 2024-06-29 16:55:05.042984

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e1de6f363c0'
down_revision = '5e12ed2c8ffb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', sa.String(length=200), nullable=True))
        batch_op.alter_column('content',
               existing_type=sa.VARCHAR(length=1000),
               type_=sa.String(length=5000),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.alter_column('content',
               existing_type=sa.String(length=5000),
               type_=sa.VARCHAR(length=1000),
               existing_nullable=True)
        batch_op.drop_column('image')

    # ### end Alembic commands ###