"""add readers

Revision ID: 0c618c83b125
Revises: 
Create Date: 2024-01-15 20:26:27.367934

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0c618c83b125'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('readers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('books', sa.Column('pages', sa.Integer(), nullable=True))
    op.add_column('books', sa.Column('reader_id', sa.Integer(), nullable=False))
    op.create_index(op.f('ix_books_reader_id'), 'books', ['reader_id'], unique=False)
    op.create_foreign_key(None, 'books', 'readers', ['reader_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'books', type_='foreignkey')
    op.drop_index(op.f('ix_books_reader_id'), table_name='books')
    op.drop_column('books', 'reader_id')
    op.drop_column('books', 'pages')
    op.drop_table('readers')
    # ### end Alembic commands ###
