"""Create table Route

Revision ID: c3c4c2b0f62a
Revises: c6b716fd1082
Create Date: 2022-06-21 18:03:49.074578

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = 'c3c4c2b0f62a'
down_revision = 'c6b716fd1082'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('route',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('number', sa.String(length=6), nullable=False),
    sa.Column('type_name', sa.String(length=12), nullable=False),
    sa.ForeignKeyConstraint(['type_name'], ['type.name'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('route')
    # ### end Alembic commands ###
