"""Rename Type.name to id

Revision ID: c58db53a9281
Revises: 9ecb9160838d
Create Date: 2022-07-15 20:00:51.245599

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2


# revision identifiers, used by Alembic.
revision = 'c58db53a9281'
down_revision = '9ecb9160838d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('route_type_name_fkey', 'route', type_='foreignkey')
    op.alter_column('route', 'type_name', new_column_name='type_id')
    op.alter_column('type', 'name', new_column_name='id')
    op.create_foreign_key('route_type_id_fkey', 'route', 'type', ['type_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('route_type_id_fkey', 'route', type_='foreignkey')
    op.alter_column('route', 'type_id', new_column_name='type_name')
    op.alter_column('type', 'id', new_column_name='name')
    op.create_foreign_key('route_type_name_fkey', 'route', 'type', ['type_name'], ['name'])
    # ### end Alembic commands ###
