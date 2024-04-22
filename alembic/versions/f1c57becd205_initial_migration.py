"""initial migration

Revision ID: f1c57becd205
Revises: 
Create Date: 2024-04-22 17:24:23.969750

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f1c57becd205'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('interventions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('kelurahan_name', sa.String(length=255), nullable=False),
    sa.Column('puskesmas_id', sa.Integer(), nullable=True),
    sa.Column('intervention_1', sa.Text(), nullable=True),
    sa.Column('intervention_2', sa.Text(), nullable=True),
    sa.Column('intervention_3', sa.Text(), nullable=True),
    sa.Column('intervention_4', sa.Text(), nullable=True),
    sa.Column('intervention_5', sa.Text(), nullable=True),
    sa.Column('intervention_6', sa.Text(), nullable=True),
    sa.Column('intervention_7', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_interventions_id'), 'interventions', ['id'], unique=False)
    op.create_index(op.f('ix_interventions_kelurahan_name'), 'interventions', ['kelurahan_name'], unique=False)
    op.create_table('surveys',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('kelurahan_id', sa.Integer(), nullable=False),
    sa.Column('kelurahan_name', sa.String(length=255), nullable=False),
    sa.Column('population_density', sa.Integer(), nullable=True),
    sa.Column('population', sa.Integer(), nullable=True),
    sa.Column('tb_cases', sa.Integer(), nullable=True),
    sa.Column('population_tb_cases_ratio', sa.Float(), nullable=True),
    sa.Column('dm_cases', sa.Integer(), nullable=True),
    sa.Column('jumlah_klinik_pratama', sa.Integer(), nullable=True),
    sa.Column('jumlah_klinik_utama', sa.Integer(), nullable=True),
    sa.Column('gender_perempuan', sa.Integer(), nullable=True),
    sa.Column('gender_laki_laki', sa.Integer(), nullable=True),
    sa.Column('usia_paruh_baya', sa.Integer(), nullable=True),
    sa.Column('usia_pensiun', sa.Integer(), nullable=True),
    sa.Column('usia_pekerja_awal', sa.Integer(), nullable=True),
    sa.Column('usia_lanjut', sa.Integer(), nullable=True),
    sa.Column('usia_muda', sa.Integer(), nullable=True),
    sa.Column('usia_pra_pensiun', sa.Integer(), nullable=True),
    sa.Column('usia_anak', sa.Integer(), nullable=True),
    sa.Column('pendidikan_diploma', sa.Integer(), nullable=True),
    sa.Column('pendidikan_s1', sa.Integer(), nullable=True),
    sa.Column('pendidikan_s2_s3', sa.Integer(), nullable=True),
    sa.Column('pendidikan_tamat_sd', sa.Integer(), nullable=True),
    sa.Column('pendidikan_tamat_sma', sa.Integer(), nullable=True),
    sa.Column('pendidikan_tamat_smp', sa.Integer(), nullable=True),
    sa.Column('pendidikan_tidak_sekolah', sa.Integer(), nullable=True),
    sa.Column('pendidikan_tidak_tamat_sd', sa.Integer(), nullable=True),
    sa.Column('status_bekerja_tidak_bekerja', sa.Integer(), nullable=True),
    sa.Column('status_bekerja_bekerja', sa.Integer(), nullable=True),
    sa.Column('pendapatan_keluarga_kategori_1', sa.Integer(), nullable=True),
    sa.Column('pendapatan_keluarga_kategori_2', sa.Integer(), nullable=True),
    sa.Column('pendapatan_keluarga_kategori_3', sa.Integer(), nullable=True),
    sa.Column('pendapatan_keluarga_kategori_4', sa.Integer(), nullable=True),
    sa.Column('pendapatan_keluarga_kategori_5', sa.Integer(), nullable=True),
    sa.Column('tpt_serumah_tidak_mendapatkan_tpt', sa.Integer(), nullable=True),
    sa.Column('tpt_serumah_tidak_ada', sa.Integer(), nullable=True),
    sa.Column('tpt_serumah_ada', sa.Integer(), nullable=True),
    sa.Column('perokok_aktif_tidak', sa.Integer(), nullable=True),
    sa.Column('perokok_aktif_ya', sa.Integer(), nullable=True),
    sa.Column('konsumsi_alkohol_tidak', sa.Integer(), nullable=True),
    sa.Column('konsumsi_alkohol_ya', sa.Integer(), nullable=True),
    sa.Column('kategori_pengetahuan_cukup', sa.Integer(), nullable=True),
    sa.Column('kategori_pengetahuan_kurang', sa.Integer(), nullable=True),
    sa.Column('kategori_pengetahuan_baik', sa.Integer(), nullable=True),
    sa.Column('kategori_pengetahuan_buruk', sa.Integer(), nullable=True),
    sa.Column('kategori_literasi_problematic', sa.Integer(), nullable=True),
    sa.Column('kategori_literasi_excellent', sa.Integer(), nullable=True),
    sa.Column('kategori_literasi_inadequate', sa.Integer(), nullable=True),
    sa.Column('kategori_literasi_sufficient', sa.Integer(), nullable=True),
    sa.Column('kategori_stigma_tinggi', sa.Integer(), nullable=True),
    sa.Column('kategori_stigma_sedang', sa.Integer(), nullable=True),
    sa.Column('kategori_stigma_rendah', sa.Integer(), nullable=True),
    sa.Column('kategori_stigma_tidak', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_surveys_created_at'), 'surveys', ['created_at'], unique=False)
    op.create_index(op.f('ix_surveys_id'), 'surveys', ['id'], unique=False)
    op.create_index(op.f('ix_surveys_kelurahan_id'), 'surveys', ['kelurahan_id'], unique=False)
    op.create_index(op.f('ix_surveys_kelurahan_name'), 'surveys', ['kelurahan_name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_surveys_kelurahan_name'), table_name='surveys')
    op.drop_index(op.f('ix_surveys_kelurahan_id'), table_name='surveys')
    op.drop_index(op.f('ix_surveys_id'), table_name='surveys')
    op.drop_index(op.f('ix_surveys_created_at'), table_name='surveys')
    op.drop_table('surveys')
    op.drop_index(op.f('ix_interventions_kelurahan_name'), table_name='interventions')
    op.drop_index(op.f('ix_interventions_id'), table_name='interventions')
    op.drop_table('interventions')
    # ### end Alembic commands ###
