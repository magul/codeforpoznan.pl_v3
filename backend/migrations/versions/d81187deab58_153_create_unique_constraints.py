"""153_create_unique_constraints

Revision ID: d81187deab58
Revises: e77f6676bf8a
Create Date: 2020-02-26 18:54:51.187603

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "d81187deab58"
down_revision = "e77f6676bf8a"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("hacknight", "date", existing_type=sa.DATE(), nullable=False)
    op.create_unique_constraint(None, "hacknight", ["date"])
    op.alter_column(
        "participant", "email", existing_type=sa.VARCHAR(length=200), nullable=False
    )
    op.alter_column(
        "participant", "first_name", existing_type=sa.VARCHAR(length=50), nullable=False
    )
    op.alter_column(
        "participant", "github", existing_type=sa.VARCHAR(length=200), nullable=False
    )
    op.alter_column(
        "participant", "last_name", existing_type=sa.VARCHAR(length=50), nullable=False
    )
    op.create_unique_constraint(None, "participant", ["email"])
    op.create_unique_constraint(None, "participant", ["github"])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "participant", type_="unique")
    op.drop_constraint(None, "participant", type_="unique")
    op.alter_column(
        "participant", "last_name", existing_type=sa.VARCHAR(length=50), nullable=True
    )
    op.alter_column(
        "participant", "github", existing_type=sa.VARCHAR(length=200), nullable=True
    )
    op.alter_column(
        "participant", "first_name", existing_type=sa.VARCHAR(length=50), nullable=True
    )
    op.alter_column(
        "participant", "email", existing_type=sa.VARCHAR(length=200), nullable=True
    )
    op.drop_constraint(None, "hacknight", type_="unique")
    op.alter_column("hacknight", "date", existing_type=sa.DATE(), nullable=True)
    # ### end Alembic commands ###
