"""add product model

Revision ID: 6cb360748a37
Revises: 
Create Date: 2022-03-22 22:44:09.111627

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6cb360748a37'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('brand', sa.String(), nullable=True),
    sa.Column('model', sa.String(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('production_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_product_brand'), 'product', ['brand'], unique=False)
    op.create_index(op.f('ix_product_id'), 'product', ['id'], unique=False)
    op.create_index(op.f('ix_product_model'), 'product', ['model'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_product_model'), table_name='product')
    op.drop_index(op.f('ix_product_id'), table_name='product')
    op.drop_index(op.f('ix_product_brand'), table_name='product')
    op.drop_table('product')
    # ### end Alembic commands ###
