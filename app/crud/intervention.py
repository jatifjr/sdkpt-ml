import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Optional
from sklearn.preprocessing import StandardScaler
from sqlalchemy.orm import Session
from app.models.intervention import Intervention
from app.models.kelurahan import Kelurahan
from app.schemas.intervention import InterventionCreate
import logging

logger = logging.getLogger(__name__)


class InterventionService:
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

        # Define feature categories
        self.feature_categories = {
            'Personel': [
                'Pasien_EfekSampingObat_Tidak',
                'Pasien_EfekSampingObat_Ya',
                'Pasien_PengaruhPendapatan_Tidak',
                'Pasien_PengaruhPendapatan_Ya',
                'Pasien_StatusBekerja_Bekerja',
                'Pasien_StatusBekerja_TidakBekerja',
                'Pasien_StatusBekerja_BelumBekerja',
                'Keluarga_StatusBekerja_Bekerja',
                'Keluarga_StatusBekerja_TidakBekerja',
                'Keluarga_RiwayatTBdiRumah_Ada',
                'Keluarga_RiwayatTBdiRumah_TidakAda',
                'Keluarga_TPTSerumah_Ada',
                'Keluarga_TPTSerumah_TidakAda',
                'Masyarakat_StatusPerkajaan_Bekerja',
                'Masyarakat_StatusPerkajaan_TidakBekerja',
            ],
            'Therapy': [
                'Keluarga_TPTSerumah_Ada',
                'Keluarga_TPTSerumah_TidakAda',
                'Pasien_KategoriBMI_BeratBadanKurang',
                'Pasien_KategoriBMI_BeratBadanNormal',
                'Pasien_KategoriBMI_KelebihanBeratBadan',
                'Pasien_KategoriBMI_obesitasI',
                'Pasien_KategoriBMI_obesitasII',
            ],
            'Education': [
                'Pasien_KategoriPengetahuan_Baik',
                'Pasien_KategoriPengetahuan_Buruk',
                'Pasien_KategoriPengetahuan_Cukup',
                'Pasien_KategoriPengetahuan_Kurang',
                'Keluarga_KategoriPengetahuan_Baik',
                'Keluarga_KategoriPengetahuan_Buruk',
                'Keluarga_KategoriPengetahuan_Cukup',
                'Keluarga_KategoriPengetahuan_Kurang',
                'Masyarakat_KategoriPengetahuan_Baik',
                'Masyarakat_KategoriPengetahuan_Buruk',
                'Masyarakat_KategoriPengetahuan_Cukup',
                'Masyarakat_KategoriPengetahuan_Kurang',
            ],
            'Social': [
                'Pasien_KategoriLiterasi_Excellent',
                'Pasien_KategoriLiterasi_Inadequate',
                'Pasien_KategoriLiterasi_Problematic',
                'Pasien_KategoriLiterasi_Sufficient',
                'Pasien_KategoriStigma_TidakStigma',
                'Pasien_KategoriStigma_StigmaRendah',
                'Pasien_KategoriStigma_StigmaSangatRendah',
                'Pasien_KategoriStigma_StigmaSedang',
                'Pasien_KategoriStigma_StigmaTinggi',
                'Keluarga_KategoriLiterasi_Inadequate',
                'Keluarga_KategoriLiterasi_Problematic',
                'Keluarga_KategoriLiterasi_Sufficient',
                'Keluarga_KategoriLiterasi_Excellent',
                'Keluarga_KategoriStigma_StigmaRendah',
                'Keluarga_KategoriStigma_StigmaSangatRendah',
                'Keluarga_KategoriStigma_StigmaSedang',
                'Keluarga_KategoriStigma_StigmaTinggi',
                'Keluarga_KategoriStigma_TidakStigma',
                'Masyarakat_KategoriLiterasi_Excellent',
                'Masyarakat_KategoriLiterasi_Inadequate',
                'Masyarakat_KategoriLiterasi_Problematic',
                'Masyarakat_KategoriLiterasi_Sufficient',
                'Masyarakat_KategoriStigma_TidakStigma',
                'Masyarakat_KategoriStigma_StigmaRendah',
                'Masyarakat_KategoriStigma_StigmaSangatRendah',
                'Masyarakat_KategoriStigma_StigmaSedang',
                'Masyarakat_KategoriStigma_StigmaTinggi',
            ],
            'Facility': [
                'Kepadatan Penduduk',
                'Jumlah Penduduk',
                'Jumlah Kasus TB',
                'rasio Pasien dan Jumlah Penduduk/10000',
                'Jumlah Kasus DM',
                'Prevalensi DM/1000',
                'Jumlah Klinik Pratama',
                'Jumlah Klinik Utama',
                'Rasio penduduk dengan Fasyankes',
                'Jumlah Puskesmas (Jadi satu dengan klinik untuk rasio)',
            ],
            'Conseling': [
                'Pasien_PendapatanKeluarga_Kategori1',
                'Pasien_PendapatanKeluarga_Kategori2',
                'Pasien_PendapatanKeluarga_Kategori3',
                'Pasien_PendapatanKeluarga_kategori4',
                'Pasien_PendapatanKeluarga_Kategori5',
                'Pasien_KategoriBMI_BeratBadanKurang',
                'Pasien_KategoriBMI_BeratBadanNormal',
                'Pasien_KategoriBMI_KelebihanBeratBadan',
                'Pasien_KategoriBMI_obesitasI',
                'Pasien_KategoriBMI_obesitasII',
                'Keluarga_JenisLantai_Kayu',
                'Keluarga_JenisLantai_Tanah',
                'Keluarga_JenisLantai_Ubin/keramik/tegel',
                'Keluarga_CahayaMataharimasuk_Tidak',
                'Keluarga_CahayaMataharimasuk_Ya',
                'Masyarakat_KategoriPendapatan_Kategori1',
                'Masyarakat_KategoriPendapatan_Kategori2',
                'Masyarakat_KategoriPendapatan_Kategori3',
                'Masyarakat_KategoriPendapatan_kategori4',
                'Masyarakat_KategoriPendapatan_Kategori5',
            ],
            'Community': [
                'Pasien_KategoriPerilaku_Baik',
                'Pasien_KategoriPerilaku_Cukup',
                'Pasien_KategoriPerilaku_Kurang',
                'Pasien_KategoriPerilaku_SangatKurang',
                'Keluarga_KategoriPerilaku_Baik',
                'Keluarga_KategoriPerilaku_Cukup',
                'Keluarga_KategoriPerilaku_Kurang',
                'Keluarga_KategoriPerilaku_SangatKurang',
                'Masyarakat_KategoriPerilaku_Baik',
                'Masyarakat_KategoriPerilaku_Cukup',
                'Masyarakat_KategoriPerilaku_Kurang',
                'Masyarakat_KategoriPerilaku_SangatKurang',
            ]
        }

        # Define intervention categories
        self.intervention_categories = {
            'Personel': [
                "Peningkatan kapasitas petugas terkait teknik komunikasi kepada pasien dan keluarga"
            ],
            'Therapy': [
                "Optimalisasi pemberian TPT"
            ],
            'Education': [
                "Penyuluhan tingkat kelurahan tentang 10 indikator PHBS"
            ],
            'Social': [
                "Penyuluhan tingkat kelurahan dan memperbanyak media Komunikasi Informasi Edukasi (KIE) untuk masyarakat tentang pencegahan dan pengobatan TBC"
            ],
            'Facility': [
                "Peningkatan kualitas layanan fasyankes"
            ],
            'Conseling': [
                "Peningkatan pelayanan konseling Upaya Berhenti Merokok (UBM) dan perluasan KTR"
            ],
            'Community': [
                "Pemberdayaan masyarakat sebagai PMO serta kader TBC di lingkungan masyarakat"
            ]
        }

    def load_data(self, file_path):
        # Load data from Excel file
        data = pd.read_excel(file_path)
        return data

    def compute_category_scores(self, data):
        # Normalize the data
        scaler = StandardScaler()
        normalized_data = scaler.fit_transform(data[list(self.weights.keys())])

        # Apply weights and compute scores for each feature
        for idx, feature in enumerate(self.weights.keys()):
            weight = self.weights[feature]
            normalized_data[:, idx] *= weight

        # Initialize an empty DataFrame to store category scores
        category_scores = pd.DataFrame(index=data.index)

        # Compute scores for each category
        for category, features in self.feature_categories.items():
            category_data = normalized_data[:, [
                list(self.weights.keys()).index(feature) for feature in features]]
            category_scores[f'{category}_Score'] = category_data.sum(axis=1)

        # Combine the category scores with the original data
        data = pd.concat([data, category_scores], axis=1)

        return data

    def rank_interventions_by_category_scores(self, category_scores):
        # Sort categories by score descending
        ranked_categories = sorted(
            category_scores.items(), key=lambda x: x[1], reverse=True)

        # Create a list to store interventions in ranked order
        ranked_interventions = []

        # Rank interventions based on the highest scoring category
        for category, _ in ranked_categories:
            interventions = self.intervention_categories.get(category, [])
            ranked_interventions.extend(interventions)

        # Fill the list with None to ensure there are exactly 7 interventions
        ranked_interventions += [None] * (7 - len(ranked_interventions))

        return ranked_interventions[:7]

    def compute_and_update_interventions(self, db: Session, file_path: str):
        # Load data from Excel file
        data = self.load_data(file_path)

        # Compute category scores for each row
        data = self.compute_category_scores(data)

        # Fetch kelurahan data to get id and puskesmas_id
        kelurahan_data = db.query(Kelurahan).all()
        kelurahan_map = {kelurahan.kelurahan_name: (
            kelurahan.id, kelurahan.puskesmas_id) for kelurahan in kelurahan_data}

        # Initialize a list to store highest scoring interventions for each row
        highest_scoring_interventions = []

        # Iterate through each row and compute interventions
        for index, row in data.iterrows():
            # Compute category scores for the current row
            category_scores = {category: row[f'{category}_Score']
                               for category in self.feature_categories}

            # Rank interventions based on the category scores
            interventions = self.rank_interventions_by_category_scores(
                category_scores)

            # Retrieve kelurahan information
            # Adjust this to match your column name
            kelurahan_name = row['Kelurahan']
            kelurahan_id, puskesmas_id = kelurahan_map.get(
                kelurahan_name, (None, None))

            # Append to the list of highest scoring interventions
            highest_scoring_interventions.append({
                'index': index + 1,
                'kelurahan_name': kelurahan_name,
                'puskesmas_id': puskesmas_id,
                'interventions': interventions
            })

        # Clear existing interventions in the Intervention table
        db.query(Intervention).delete()

        # Update the Intervention table with the highest scoring interventions
        for data in highest_scoring_interventions:
            db_intervention = Intervention(
                id=data['index'],  # Set the id as the index
                kelurahan_name=data['kelurahan_name'],
                puskesmas_id=data['puskesmas_id'],
                intervention_1=data['interventions'][0] if len(
                    data['interventions']) > 0 else None,
                intervention_2=data['interventions'][1] if len(
                    data['interventions']) > 1 else None,
                intervention_3=data['interventions'][2] if len(
                    data['interventions']) > 2 else None,
                intervention_4=data['interventions'][3] if len(
                    data['interventions']) > 3 else None,
                intervention_5=data['interventions'][4] if len(
                    data['interventions']) > 4 else None,
                intervention_6=data['interventions'][5] if len(
                    data['interventions']) > 5 else None,
                intervention_7=data['interventions'][6] if len(
                    data['interventions']) > 6 else None,
            )
            db.add(db_intervention)
            db.commit()

        return highest_scoring_interventions

    def get_all(self, db: Session):
        # Retrieve all records from the database
        return db.query(Intervention).all()

    def get_by_kelurahan_id(self, db: Session, kelurahan_id: int) -> Optional[Intervention]:
        # Retrieve a record by Kelurahan ID from the database
        return db.query(Intervention).filter(Intervention.id == kelurahan_id).first()
