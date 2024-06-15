import os
import pickle
import pandas as pd
import numpy as np
from typing import Dict, List, Tuple
from sklearn.preprocessing import StandardScaler
# from sklearn.ensemble import RandomForestClassifier
from sqlalchemy import func, and_
from sqlalchemy.orm import Session
from app.models.kerentanan import Kerentanan
from app.models.upload_survey import UploadSurvey
from app.schemas.kerentanan import KerentananCreate
import logging

logger = logging.getLogger(__name__)


class VulnerabilityService:
    def __init__(self):

        # Define weights for each feature for vulnerability scoring
        self.weights = {
            'Kepadatan Penduduk': 1,
            'Jumlah Penduduk': 0,  # Not used in scoring
            'Jumlah Kasus TB': 1,
            'rasio Pasien dan Jumlah Penduduk/10000': 1,
            'Jumlah Kasus DM': 1,
            'Prevalensi DM/1000': 1,
            'Jumlah Klinik Pratama': -1,
            'Jumlah Klinik Utama': -1,
            'Rasio penduduk dengan Fasyankes': -1,
            'Jumlah Puskesmas (Jadi satu dengan klinik untuk rasio)': -1,
            'Pasien_JenisKelamin_Laki-laki': 1,
            'Pasien_JenisKelamin_Perempuan': -1,
            'Pasien_PendidikanTerakhir_Diploma': -1,
            'Pasien_PendidikanTerakhir_S1': -1,
            'Pasien_PendidikanTerakhir_S2/S3': -1,
            'Pasien_PendidikanTerakhir_TamatSD': 1,
            'Pasien_PendidikanTerakhir_TamatSMA/Sederajat': 1,
            'Pasien_PendidikanTerakhir_TamatSMP/Sederajat': 1,
            'Pasien_PendidikanTerakhir_TidakSekolah': 1,
            'Pasien_PendidikanTerakhir_TidakTamatSD': 1,
            'Pasien_StatusBekerja_Bekerja': 1,
            'Pasien_StatusBekerja_TidakBekerja': -1,
            'Pasien_StatusBekerja_BelumBekerja': -1,
            'Pasien_PendapatanKeluarga_Kategori1': 1,
            'Pasien_PendapatanKeluarga_Kategori2': 1,
            'Pasien_PendapatanKeluarga_Kategori3': 1,
            'Pasien_PendapatanKeluarga_kategori4': -1,
            'Pasien_PendapatanKeluarga_Kategori5': -1,
            'Pasien_EfekSampingObat_Tidak': -1,
            'Pasien_EfekSampingObat_Ya': 1,
            'Pasien_PengaruhPendapatan_Tidak': -1,
            'Pasien_PengaruhPendapatan_Ya': 1,
            'Pasien_KategoriBMI_BeratBadanKurang': 1,
            'Pasien_KategoriBMI_BeratBadanNormal': -1,
            'Pasien_KategoriBMI_KelebihanBeratBadan': 1,
            'Pasien_KategoriBMI_obesitasI': 1,
            'Pasien_KategoriBMI_obesitasII': 1,
            'Pasien_KategoriUsia_Anak-Anak': 1,
            'Pasien_KategoriUsia_Balita': 1,
            'Pasien_KategoriUsia_DewasaAkhir': 1,
            'Pasien_KategoriUsia_DewasaAwal': 1,
            'Pasien_KategoriUsia_LansiaAkhir': 1,
            'Pasien_KategoriUsia_LansiaAwal': 1,
            'Pasien_KategoriUsia_Manula': 1,
            'Pasien_KategoriUsia_RemajaAkhir': 1,
            'Pasien_KategoriUsia_RemajaAwal': 1,
            'Pasien_KategoriPengetahuan_Baik': -1,
            'Pasien_KategoriPengetahuan_Buruk': 1,
            'Pasien_KategoriPengetahuan_Cukup': -1,
            'Pasien_KategoriPengetahuan_Kurang': 1,
            'Pasien_KategoriPerilaku_Baik': -1,
            'Pasien_KategoriPerilaku_Cukup': -1,
            'Pasien_KategoriPerilaku_Kurang': 1,
            'Pasien_KategoriPerilaku_SangatKurang': 1,
            'Pasien_KategoriLiterasi_Excellent': -1,
            'Pasien_KategoriLiterasi_Inadequate': 1,
            'Pasien_KategoriLiterasi_Problematic': 1,
            'Pasien_KategoriLiterasi_Sufficient': -1,
            'Pasien_KategoriStigma_TidakStigma': -1,
            'Pasien_KategoriStigma_StigmaRendah': -1,
            'Pasien_KategoriStigma_StigmaSangatRendah': -1,
            'Pasien_KategoriStigma_StigmaSedang': 1,
            'Pasien_KategoriStigma_StigmaTinggi': 1,
            'Keluarga_PendidikanTerakhir_Diploma': -1,
            'Keluarga_PendidikanTerakhir_S1': -1,
            'Keluarga_PendidikanTerakhir_S2/S3': -1,
            'Keluarga_PendidikanTerakhir_TamatSD': 1,
            'Keluarga_PendidikanTerakhir_TamatSMA/Sederajat': 1,
            'Keluarga_PendidikanTerakhir_TamatSMP/Sederajat': 1,
            'Keluarga_PendidikanTerakhir_TidakSekolah': 1,
            'Keluarga_PendidikanTerakhir_TidakTamatSD': 1,
            'Keluarga_StatusBekerja_Bekerja': 1,
            'Keluarga_StatusBekerja_TidakBekerja': -1,
            'Keluarga_RiwayatTBdiRumah_Ada': 1,
            'Keluarga_RiwayatTBdiRumah_TidakAda': -1,
            'Keluarga_TPTSerumah_Ada': -1,
            'Keluarga_TPTSerumah_TidakAda': 1,
            'Keluarga_JenisLantai_Kayu': 1,
            'Keluarga_JenisLantai_Tanah': 1,
            'Keluarga_JenisLantai_Ubin/keramik/tegel': -1,
            'Keluarga_CahayaMataharimasuk_Tidak': 1,
            'Keluarga_CahayaMataharimasuk_Ya': -1,
            'Keluarga_KategoriPengetahuan_Baik': -1,
            'Keluarga_KategoriPengetahuan_Buruk': 1,
            'Keluarga_KategoriPengetahuan_Cukup': -1,
            'Keluarga_KategoriPengetahuan_Kurang': 1,
            'Keluarga_KategoriLiterasi_Inadequate': 1,
            'Keluarga_KategoriLiterasi_Problematic': 1,
            'Keluarga_KategoriLiterasi_Sufficient': -1,
            'Keluarga_KategoriLiterasi_Excellent': -1,
            'Keluarga_KategoriStigma_StigmaRendah': -1,
            'Keluarga_KategoriStigma_StigmaSangatRendah': -1,
            'Keluarga_KategoriStigma_StigmaSedang': 1,
            'Keluarga_KategoriStigma_StigmaTinggi': 1,
            'Keluarga_KategoriStigma_TidakStigma': -1,
            'Keluarga_KategoriPerilaku_Baik': -1,
            'Keluarga_KategoriPerilaku_Cukup': -1,
            'Keluarga_KategoriPerilaku_Kurang': 1,
            'Keluarga_KategoriPerilaku_SangatKurang': 1,
            'Masyarakat_PendidikanTerakhir_Diploma': -1,
            'Masyarakat_PendidikanTerakhir_S1': -1,
            'Masyarakat_PendidikanTerakhir_S2/S3': -1,
            'Masyarakat_PendidikanTerakhir_TamatSD': 1,
            'Masyarakat_PendidikanTerakhir_TamatSMA/Sederajat': 1,
            'Masyarakat_PendidikanTerakhir_TamatSMP/Sederajat': 1,
            'Masyarakat_PendidikanTerakhir_TidakSekolah': 1,
            'Masyarakat_PendidikanTerakhir_TidakTamatSD': 1,
            'Masyarakat_StatusPerkajaan_Bekerja': 1,
            'Masyarakat_StatusPerkajaan_TidakBekerja': -1,
            'Masyarakat_KategoriPendapatan_Kategori1': 1,
            'Masyarakat_KategoriPendapatan_Kategori2': 1,
            'Masyarakat_KategoriPendapatan_Kategori3': 1,
            'Masyarakat_KategoriPendapatan_kategori4': -1,
            'Masyarakat_KategoriPendapatan_Kategori5': -1,
            'Masyarakat_KategoriLiterasi_Excellent': -1,
            'Masyarakat_KategoriLiterasi_Inadequate': 1,
            'Masyarakat_KategoriLiterasi_Problematic': 1,
            'Masyarakat_KategoriLiterasi_Sufficient': -1,
            'Masyarakat_KategoriPengetahuan_Baik': -1,
            'Masyarakat_KategoriPengetahuan_Buruk': 1,
            'Masyarakat_KategoriPengetahuan_Cukup': -1,
            'Masyarakat_KategoriPengetahuan_Kurang': 1,
            'Masyarakat_KategoriStigma_TidakStigma': -1,
            'Masyarakat_KategoriStigma_StigmaRendah': -1,
            'Masyarakat_KategoriStigma_StigmaSangatRendah': -1,
            'Masyarakat_KategoriStigma_StigmaSedang': 1,
            'Masyarakat_KategoriStigma_StigmaTinggi': 1,
            'Masyarakat_KategoriPerilaku_Baik': -1,
            'Masyarakat_KategoriPerilaku_Cukup': -1,
            'Masyarakat_KategoriPerilaku_Kurang': 1,
            'Masyarakat_KategoriPerilaku_SangatKurang': 1,
        }

    def load_data(self, file_path):
        # Load data from Excel file
        data = pd.read_excel(file_path)
        return data

    def compute_vulnerability_scores(self, data):
        # Normalize the data
        scaler = StandardScaler()
        normalized_data = scaler.fit_transform(data[list(self.weights.keys())])

        # Apply weights and compute scores
        for idx, feature in enumerate(self.weights.keys()):
            weight = self.weights[feature]
            normalized_data[:, idx] *= weight

        data['Vulnerability_Score'] = normalized_data.sum(axis=1)

        return data

    def merge_data(self, original_data, scored_data):
        # Merge scored data with original data
        merged_data = pd.merge(original_data, scored_data[['ID Kelurahan', 'Vulnerability_Score']],
                               on='ID Kelurahan', how='left', suffixes=('', '_y'))

        # Define vulnerability levels
        merged_data['Vulnerability_Level'] = pd.qcut(merged_data['Vulnerability_Score'], q=4, labels=[
            'Tidak Rentan', 'Cukup Rentan', 'Rentan', 'Sangat Rentan'])

        return merged_data

    def create_bulk(self, db: Session, data: pd.DataFrame):
        # Iterate through each row in the DataFrame
        for _, row in data.iterrows():
            # Check if a record with the same kelurahan already exists
            existing_record = db.query(Kerentanan).filter(
                Kerentanan.kelurahan == row['Kelurahan']).first()

            if existing_record:
                # If record exists, update the kategori_kerentanan value
                update_data = {
                    'kategori_kerentanan': row['Vulnerability_Level']
                }
                db.query(Kerentanan).filter(Kerentanan.id ==
                                            existing_record.id).update(update_data)

            else:
                # If record does not exist, create a new record
                db_obj = KerentananCreate(
                    kelurahan=row['Kelurahan'],
                    jumlah_kasus=row['Jumlah Kasus TB'],
                    kategori_kerentanan=row['Vulnerability_Level']
                )
                db.add(Kerentanan(**db_obj.dict()))

        # Commit the transaction
        db.commit()

    def get_all(self, db: Session):
        # Retrieve all records from the database
        return db.query(Kerentanan).all()

    def get_by_kelurahan_id(self, db: Session, kelurahan_id: int):
        # Retrieve a record by Kelurahan ID from the database
        return db.query(Kerentanan).filter(Kerentanan.id == kelurahan_id).first()
