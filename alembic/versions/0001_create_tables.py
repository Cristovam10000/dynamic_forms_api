"""create tables

Revision ID: 0001
Revises: 
Create Date: 2024-11-07 00:00:00.000000

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'formulario',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('titulo', sa.String(), nullable=False),
        sa.Column('descricao', sa.Text(), nullable=True),
        sa.Column('ordem', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_formulario_id', 'formulario', ['id'], unique=False)

    op.create_table(
        'pergunta',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('id_formulario', sa.Integer(), nullable=False),
        sa.Column('titulo', sa.String(), nullable=False),
        sa.Column('codigo', sa.String(), nullable=True),
        sa.Column('orientacao_resposta', sa.Text(), nullable=True),
        sa.Column('ordem', sa.Integer(), nullable=True),
        sa.Column('obrigatoria', sa.Boolean(), nullable=True),
        sa.Column('sub_pergunta', sa.Boolean(), nullable=True),
        sa.Column('tipo_pergunta', sa.Enum('sim_nao','mult_escolha','unica_escolha','texto_livre','inteiro','decimal', name='tipopergunta'), nullable=False),
        sa.ForeignKeyConstraint(['id_formulario'], ['formulario.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_pergunta_id', 'pergunta', ['id'], unique=False)
    op.create_index('ix_pergunta_codigo', 'pergunta', ['codigo'], unique=True)

    op.create_table(
        'opcoes_respostas',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('id_pergunta', sa.Integer(), nullable=True),
        sa.Column('resposta', sa.String(), nullable=False),
        sa.Column('ordem', sa.Integer(), nullable=True),
        sa.Column('resposta_aberta', sa.Boolean(), nullable=True),
        sa.ForeignKeyConstraint(['id_pergunta'], ['pergunta.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'opcoes_resposta_pergunta',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('id_opcao_resposta', sa.Integer(), nullable=True),
        sa.Column('id_pergunta', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['id_opcao_resposta'], ['opcoes_respostas.id']),
        sa.ForeignKeyConstraint(['id_pergunta'], ['pergunta.id']),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('opcoes_resposta_pergunta')
    op.drop_table('opcoes_respostas')
    op.drop_index('ix_pergunta_codigo', table_name='pergunta')
    op.drop_index('ix_pergunta_id', table_name='pergunta')
    op.drop_table('pergunta')
    op.drop_index('ix_formulario_id', table_name='formulario')
    op.drop_table('formulario')
    op.execute('DROP TYPE tipopergunta')
