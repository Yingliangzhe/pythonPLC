"""empty message

Revision ID: 2671f9b6958f
Revises: 
Create Date: 2017-11-30 09:45:59.341944

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2671f9b6958f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('alarm_info', 'bool')
    op.drop_column('yjvariableinfo', 'is_upload')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('yjvariableinfo', sa.Column('is_upload', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('alarm_info', sa.Column('bool', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    # ### end Alembic commands ###