"""added upload survey

Revision ID: 987d9f8343d6
Revises: 28a58f7e8d5d
Create Date: 2024-06-05 12:38:43.853930

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '987d9f8343d6'
down_revision: Union[str, None] = '28a58f7e8d5d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('survey_upload',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('kelurahan_id', sa.Integer(), nullable=False),
    sa.Column('kecamatan', sa.String(length=255), nullable=False),
    sa.Column('kelurahan', sa.String(length=255), nullable=False),
    sa.Column('kepadatan_penduduk', sa.Integer(), nullable=True),
    sa.Column('jumlah_penduduk', sa.Integer(), nullable=True),
    sa.Column('jumlah_kasus_tb', sa.Integer(), nullable=True),
    sa.Column('rasio_pasien_dan_jumlah_penduduk', sa.Float(), nullable=True),
    sa.Column('jumlah_kasus_dm', sa.Integer(), nullable=True),
    sa.Column('prevalensi_dm', sa.Float(), nullable=True),
    sa.Column('jumlah_klinik_pratama', sa.Integer(), nullable=True),
    sa.Column('jumlah_klinik_utama', sa.Integer(), nullable=True),
    sa.Column('rasio_penduduk_dan_fasyankes', sa.Float(), nullable=True),
    sa.Column('jumlah_puskemas', sa.Integer(), nullable=True),
    sa.Column('pasien_jenis_kelamin_laki_laki', sa.Integer(), nullable=True),
    sa.Column('pasien_jenis_kelamin_perempuan', sa.Integer(), nullable=True),
    sa.Column('pasien_pendidikan_terakhir_diploma', sa.Integer(), nullable=True),
    sa.Column('pasien_pendidikan_terakhir_s1', sa.Integer(), nullable=True),
    sa.Column('pasien_pendidikan_terakhir_s2_s3', sa.Integer(), nullable=True),
    sa.Column('pasien_pendidikan_terakhir_tamat_sd', sa.Integer(), nullable=True),
    sa.Column('pasien_pendidikan_terakhir_tamat_sma_sederajat', sa.Integer(), nullable=True),
    sa.Column('pasien_pendidikan_terakhir_tamat_smp_sederajat', sa.Integer(), nullable=True),
    sa.Column('pasien_pendidikan_terakhir_tidak_sekolah', sa.Integer(), nullable=True),
    sa.Column('pasien_pendidikan_terakhir_tidak_tamat_sd', sa.Integer(), nullable=True),
    sa.Column('pasien_status_bekerja_bekerja', sa.Integer(), nullable=True),
    sa.Column('pasien_status_bekerja_tidak_bekerja', sa.Integer(), nullable=True),
    sa.Column('pasien_status_bekerja_belum_bekerja', sa.Integer(), nullable=True),
    sa.Column('pasien_pendapatan_keluarga_kategori1', sa.Integer(), nullable=True),
    sa.Column('pasien_pendapatan_keluarga_kategori2', sa.Integer(), nullable=True),
    sa.Column('pasien_pendapatan_keluarga_kategori3', sa.Integer(), nullable=True),
    sa.Column('pasien_pendapatan_keluarga_kategori4', sa.Integer(), nullable=True),
    sa.Column('pasien_pendapatan_keluarga_kategori5', sa.Integer(), nullable=True),
    sa.Column('pasien_efek_samping_obat_tidak', sa.Integer(), nullable=True),
    sa.Column('pasien_efek_samping_obat_ya', sa.Integer(), nullable=True),
    sa.Column('pasien_pengaruh_pendapatan_tidak', sa.Integer(), nullable=True),
    sa.Column('pasien_pengaruh_pendapatan_ya', sa.Integer(), nullable=True),
    sa.Column('pasien_kategori_bmi_berat_badan_kurang', sa.Integer(), nullable=True),
    sa.Column('pasien_kategori_bmi_berat_badan_normal', sa.Integer(), nullable=True),
    sa.Column('pasien_kategori_bmi_kelebihan_berat_badan', sa.Integer(), nullable=True),
    sa.Column('pasien_kategori_bmi_obesitas_i', sa.Integer(), nullable=True),
    sa.Column('pasien_kategori_bmi_obesitas_ii', sa.Integer(), nullable=True),
    sa.Column('pasien_kategori_usia_anak_anak', sa.Integer(), nullable=True),
    sa.Column('pasien_kategori_usia_balita', sa.Integer(), nullable=True),
    sa.Column('pasien_kategori_usia_dewasa_akhir', sa.Integer(), nullable=True),
    sa.Column('pasien_kategori_usia_dewasa_awal', sa.Integer(), nullable=True),
    sa.Column('pasien_kategori_usia_lansia_akhir', sa.Integer(), nullable=True),
    sa.Column('pasien_kategori_usia_lansia_awal', sa.Integer(), nullable=True),
    sa.Column('pasien_kategori_usia_manula', sa.Integer(), nullable=True),
    sa.Column('pasien_kategori_usia_remaja_akhir', sa.Integer(), nullable=True),
    sa.Column('pasien_kategori_usia_remaja_awal', sa.Integer(), nullable=True),
    sa.Column('pasien_kategori_pengetahuan_baik', sa.Integer(), nullable=True),
    sa.Column('pasien_kategori_pengetahuan_buruk', sa.Integer(), nullable=True),
    sa.Column('pasien_kategori_pengetahuan_cukup', sa.Integer(), nullable=True),
    sa.Column('pasien_kategori_pengetahuan_kurang', sa.Integer(), nullable=True),
    sa.Column('pasien_kategori_perilaku_baik', sa.Integer(), nullable=True),
    sa.Column('pasien_kategori_perilaku_cukup', sa.Integer(), nullable=True),
    sa.Column('pasien_kategori_perilaku_kurang', sa.Integer(), nullable=True),
    sa.Column('pasien_kategori_perilaku_sangat_kurang', sa.Integer(), nullable=True),
    sa.Column('pasien_kategori_literasi_excellent', sa.Integer(), nullable=True),
    sa.Column('pasien_kategori_literasi_inadequate', sa.Integer(), nullable=True),
    sa.Column('pasien_kategori_literasi_problematic', sa.Integer(), nullable=True),
    sa.Column('pasien_kategori_literasi_sufficient', sa.Integer(), nullable=True),
    sa.Column('pasien_kategori_stigma_tidak_stigma', sa.Integer(), nullable=True),
    sa.Column('pasien_kategori_stigma_stigma_rendah', sa.Integer(), nullable=True),
    sa.Column('pasien_kategori_stigma_stigma_sangat_rendah', sa.Integer(), nullable=True),
    sa.Column('pasien_kategori_stigma_stigma_sedang', sa.Integer(), nullable=True),
    sa.Column('pasien_kategori_stigma_stigma_tinggi', sa.Integer(), nullable=True),
    sa.Column('keluarga_pendidikan_terakhir_diploma', sa.Integer(), nullable=True),
    sa.Column('keluarga_pendidikan_terakhir_s1', sa.Integer(), nullable=True),
    sa.Column('keluarga_pendidikan_terakhir_s2_s3', sa.Integer(), nullable=True),
    sa.Column('keluarga_pendidikan_terakhir_tamat_sd', sa.Integer(), nullable=True),
    sa.Column('keluarga_pendidikan_terakhir_tamat_sma_sederajat', sa.Integer(), nullable=True),
    sa.Column('keluarga_pendidikan_terakhir_tamat_smp_sederajat', sa.Integer(), nullable=True),
    sa.Column('keluarga_pendidikan_terakhir_tidak_sekolah', sa.Integer(), nullable=True),
    sa.Column('keluarga_pendidikan_terakhir_tidak_tamat_sd', sa.Integer(), nullable=True),
    sa.Column('keluarga_status_bekerja_bekerja', sa.Integer(), nullable=True),
    sa.Column('keluarga_status_bekerja_tidak_bekerja', sa.Integer(), nullable=True),
    sa.Column('keluarga_riwayat_tb_di_rumah_ada', sa.Integer(), nullable=True),
    sa.Column('keluarga_riwayat_tb_di_rumah_tidak_ada', sa.Integer(), nullable=True),
    sa.Column('keluarga_tpt_serumah_ada', sa.Integer(), nullable=True),
    sa.Column('keluarga_tpt_serumah_tidak_ada', sa.Integer(), nullable=True),
    sa.Column('keluarga_jenis_lantai_kayu', sa.Integer(), nullable=True),
    sa.Column('keluarga_jenis_lantai_tanah', sa.Integer(), nullable=True),
    sa.Column('keluarga_jenis_lantai_ubin_keramik_tegel', sa.Integer(), nullable=True),
    sa.Column('keluarga_cahaya_matahari_masuk_tidak', sa.Integer(), nullable=True),
    sa.Column('keluarga_cahaya_matahari_masuk_ya', sa.Integer(), nullable=True),
    sa.Column('keluarga_kategori_pengetahuan_baik', sa.Integer(), nullable=True),
    sa.Column('keluarga_kategori_pengetahuan_buruk', sa.Integer(), nullable=True),
    sa.Column('keluarga_kategori_pengetahuan_cukup', sa.Integer(), nullable=True),
    sa.Column('keluarga_kategori_pengetahuan_kurang', sa.Integer(), nullable=True),
    sa.Column('keluarga_kategori_literasi_inadequate', sa.Integer(), nullable=True),
    sa.Column('keluarga_kategori_literasi_problematic', sa.Integer(), nullable=True),
    sa.Column('keluarga_kategori_literasi_sufficient', sa.Integer(), nullable=True),
    sa.Column('keluarga_kategori_literasi_excellent', sa.Integer(), nullable=True),
    sa.Column('keluarga_kategori_stigma_stigma_rendah', sa.Integer(), nullable=True),
    sa.Column('keluarga_kategori_stigma_stigma_sangat_rendah', sa.Integer(), nullable=True),
    sa.Column('keluarga_kategori_stigma_stigma_sedang', sa.Integer(), nullable=True),
    sa.Column('keluarga_kategori_stigma_stigma_tinggi', sa.Integer(), nullable=True),
    sa.Column('keluarga_kategori_stigma_tidak_stigma', sa.Integer(), nullable=True),
    sa.Column('keluarga_kategori_perilaku_baik', sa.Integer(), nullable=True),
    sa.Column('keluarga_kategori_perilaku_cukup', sa.Integer(), nullable=True),
    sa.Column('keluarga_kategori_perilaku_kurang', sa.Integer(), nullable=True),
    sa.Column('keluarga_kategori_perilaku_sangat_kurang', sa.Integer(), nullable=True),
    sa.Column('masyarakat_pendidikan_terakhir_diploma', sa.Integer(), nullable=True),
    sa.Column('masyarakat_pendidikan_terakhir_s1', sa.Integer(), nullable=True),
    sa.Column('masyarakat_pendidikan_terakhir_s2_s3', sa.Integer(), nullable=True),
    sa.Column('masyarakat_pendidikan_terakhir_tamat_sd', sa.Integer(), nullable=True),
    sa.Column('masyarakat_pendidikan_terakhir_tamat_sma_sederajat', sa.Integer(), nullable=True),
    sa.Column('masyarakat_pendidikan_terakhir_tamat_smp_sederajat', sa.Integer(), nullable=True),
    sa.Column('masyarakat_pendidikan_terakhir_tidak_sekolah', sa.Integer(), nullable=True),
    sa.Column('masyarakat_pendidikan_terakhir_tidak_tamat_sd', sa.Integer(), nullable=True),
    sa.Column('masyarakat_status_perkajaan_bekerja', sa.Integer(), nullable=True),
    sa.Column('masyarakat_status_perkajaan_tidak_bekerja', sa.Integer(), nullable=True),
    sa.Column('masyarakat_kategori_pendapatan_kategori1', sa.Integer(), nullable=True),
    sa.Column('masyarakat_kategori_pendapatan_kategori2', sa.Integer(), nullable=True),
    sa.Column('masyarakat_kategori_pendapatan_kategori3', sa.Integer(), nullable=True),
    sa.Column('masyarakat_kategori_pendapatan_kategori4', sa.Integer(), nullable=True),
    sa.Column('masyarakat_kategori_pendapatan_kategori5', sa.Integer(), nullable=True),
    sa.Column('masyarakat_riwayat_tb_keluarga_ada', sa.Integer(), nullable=True),
    sa.Column('masyarakat_riwayat_tb_keluarga_tidak_ada', sa.Integer(), nullable=True),
    sa.Column('masyarakat_kategori_bmi_berat_badan_kurang', sa.Integer(), nullable=True),
    sa.Column('masyarakat_kategori_bmi_berat_badan_normal', sa.Integer(), nullable=True),
    sa.Column('masyarakat_kategori_bmi_kelebihan_berat_badan', sa.Integer(), nullable=True),
    sa.Column('masyarakat_kategori_bmi_obesitas_i', sa.Integer(), nullable=True),
    sa.Column('masyarakat_kategori_bmi_obesitas_ii', sa.Integer(), nullable=True),
    sa.Column('masyarakat_kategori_pengetahuan_baik', sa.Integer(), nullable=True),
    sa.Column('masyarakat_kategori_pengetahuan_buruk', sa.Integer(), nullable=True),
    sa.Column('masyarakat_kategori_pengetahuan_cukup', sa.Integer(), nullable=True),
    sa.Column('masyarakat_kategori_pengetahuan_kurang', sa.Integer(), nullable=True),
    sa.Column('masyarakat_kategori_perilaku_baik', sa.Integer(), nullable=True),
    sa.Column('masyarakat_kategori_perilaku_cukup', sa.Integer(), nullable=True),
    sa.Column('masyarakat_kategori_perilaku_kurang', sa.Integer(), nullable=True),
    sa.Column('masyarakat_kategori_perilaku_sangat_kurang', sa.Integer(), nullable=True),
    sa.Column('masyarakat_kategori_literasi_excellent', sa.Integer(), nullable=True),
    sa.Column('masyarakat_kategori_literasi_inadequate', sa.Integer(), nullable=True),
    sa.Column('masyarakat_kategori_literasi_problematic', sa.Integer(), nullable=True),
    sa.Column('masyarakat_kategori_literasi_sufficient', sa.Integer(), nullable=True),
    sa.Column('masyarakat_kategori_stigma_stigma_rendah', sa.Integer(), nullable=True),
    sa.Column('masyarakat_kategori_stigma_stigma_sangat_rendah', sa.Integer(), nullable=True),
    sa.Column('masyarakat_kategori_stigma_stigma_sedang', sa.Integer(), nullable=True),
    sa.Column('masyarakat_kategori_stigma_stigma_tinggi', sa.Integer(), nullable=True),
    sa.Column('masyarakat_kategori_stigma_tidak_stigma', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_survey_upload_created_at'), 'survey_upload', ['created_at'], unique=False)
    op.create_index(op.f('ix_survey_upload_id'), 'survey_upload', ['id'], unique=False)
    op.create_index(op.f('ix_survey_upload_kecamatan'), 'survey_upload', ['kecamatan'], unique=False)
    op.create_index(op.f('ix_survey_upload_kelurahan'), 'survey_upload', ['kelurahan'], unique=False)
    op.create_index(op.f('ix_survey_upload_kelurahan_id'), 'survey_upload', ['kelurahan_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_survey_upload_kelurahan_id'), table_name='survey_upload')
    op.drop_index(op.f('ix_survey_upload_kelurahan'), table_name='survey_upload')
    op.drop_index(op.f('ix_survey_upload_kecamatan'), table_name='survey_upload')
    op.drop_index(op.f('ix_survey_upload_id'), table_name='survey_upload')
    op.drop_index(op.f('ix_survey_upload_created_at'), table_name='survey_upload')
    op.drop_table('survey_upload')
    # ### end Alembic commands ###
