"""Fix VARCHAR length for MySQL

Revision ID: f126218d692c
Revises: b13c04d32fea
Create Date: 2025-03-20 22:02:22.556567

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'f126218d692c'
down_revision: Union[str, None] = 'b13c04d32fea'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    op.drop_index('email', table_name='user')
    op.drop_index('ix_user_username', table_name='user')
    op.drop_table('user')
    op.drop_index('ix_comment_content', table_name='comment')
    op.drop_table('comment')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comment',
    sa.Column('comment_id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('content', mysql.VARCHAR(length=450), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=False),
    sa.Column('updated_at', mysql.DATETIME(), nullable=False),
    sa.Column('post_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['post.post_id'], name='comment_ibfk_1', onupdate='CASCADE'),
    sa.PrimaryKeyConstraint('comment_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_comment_content', 'comment', ['content'], unique=False)
    op.create_table('user',
    sa.Column('user_id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('first_name', mysql.VARCHAR(length=25), nullable=False),
    sa.Column('last_name', mysql.VARCHAR(length=25), nullable=False),
    sa.Column('username', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('password_hash', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('country', mysql.VARCHAR(length=25), nullable=False),
    sa.Column('city', mysql.VARCHAR(length=25), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=False),
    sa.PrimaryKeyConstraint('user_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_user_username', 'user', ['username'], unique=False)
    op.create_index('email', 'user', ['email'], unique=True)
    op.create_table('post',
    sa.Column('post_id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', mysql.VARCHAR(length=125), nullable=False),
    sa.Column('content', mysql.VARCHAR(length=450), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=False),
    sa.Column('updated_at', mysql.DATETIME(), nullable=False),
    sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], name='post_ibfk_1', onupdate='CASCADE'),
    sa.PrimaryKeyConstraint('post_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
