from alembic import op
import sqlalchemy as sa

revision = '002_add_discounts'
down_revision = '001'

def upgrade():
    op.create_table('discounts',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('precio_descuento', sa.Float(), nullable=False),
        sa.Column('fecha', sa.DateTime(timezone=True), server_default=sa.func.now()),
    )
    op.create_table('discount_items',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('discount_id', sa.Integer(), sa.ForeignKey('discounts.id'), nullable=False),
        sa.Column('product_id', sa.Integer(), sa.ForeignKey('products.id'), nullable=False),
        sa.Column('quantity', sa.Integer(), nullable=False),
    )

def downgrade():
    op.drop_table('discount_items')
    op.drop_table('discounts')