"""Films and comment

Revision ID: e8e4d9158a3a
Revises: 
Create Date: 2023-05-21 11:38:06.499628

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "e8e4d9158a3a"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "films",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("release_date", sa.DATE(), nullable=True),
        sa.Column(
            "date_created",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "film_comment",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("text", sa.String(length=500), nullable=False),
        sa.Column("film_id", sa.Integer, nullable=False),
        sa.Column(
            "date_created",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(["film_id"], ["films.id"], ondelete="NO ACTION"),
    )
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("film_comment")
    op.drop_table("films")
    pass
    # ### end Alembic commands ###
