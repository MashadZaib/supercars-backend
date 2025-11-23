"""initial migration

Revision ID: d11357299ccc
Revises: 6e382c621dec
Create Date: 2025-11-23 23:48:08.972177
"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd11357299ccc'
down_revision: Union[str, Sequence[str], None] = '6e382c621dec'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    # Correct MethodEnum type creation
    method_enum = sa.Enum(
        'Email',
        'WhatsApp',
        'Verbal',
        'In Person',
        'Other',
        name='methodenum'
    )

    # Create enum in DB
    method_enum.create(op.get_bind(), checkfirst=True)

    # Add new columns
    op.add_column('client_info', sa.Column('entry_date', sa.Date(), nullable=False))
    op.add_column('client_info', sa.Column('method_type', method_enum, nullable=False))
    op.add_column('client_info', sa.Column('address', sa.String(length=500), nullable=True))

    # Drop old columns
    op.drop_column('client_info', 'shipping_address')
    op.drop_column('client_info', 'billing_address')


def downgrade() -> None:
    """Downgrade schema."""

    method_enum = sa.Enum(name='methodenum')

    # Recreate removed columns
    op.add_column('client_info', sa.Column('billing_address', sa.String(length=500), nullable=True))
    op.add_column('client_info', sa.Column('shipping_address', sa.String(length=500), nullable=True))

    # Remove newly created columns
    op.drop_column('client_info', 'address')
    op.drop_column('client_info', 'method_type')
    op.drop_column('client_info', 'entry_date')

    # Drop enum type
    method_enum.drop(op.get_bind(), checkfirst=True)
