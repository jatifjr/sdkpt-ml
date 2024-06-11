import os
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from sqlalchemy.orm import Session
from app.models.kerentanan import Kerentanan
from app.schemas.kerentanan import KerentananCreate
import logging

logger = logging.getLogger(__name__)


class VulnerabilityService:
    def __init__(self):
        # Initialize models and directories
        self.random_forest_model = RandomForestClassifier(
            n_estimators=100, random_state=42)
        self.kmeans_model = KMeans(n_clusters=4, random_state=42)
        self.models_trained = False

        self.model_dir = 'vulnerability_models'
        if not os.path.exists(self.model_dir):
            os.makedirs(self.model_dir)

        # Define weights for each feature for vulnerability scoring
        self.weights = {
            'Kepadatan Penduduk': 1,
            'Jumlah Penduduk': 1,
            'Jumlah Kasus TB': 1,
            'rasio Pasien dan Jumlah Penduduk/10000': 1,
            'Jumlah Kasus DM': 1,
            'Prevalensi DM/1000': 1,
            'Rasio penduduk dengan Fasyankes': 1,
        }

        # Features selected for clustering
        self.cluster_features = [
            'Kepadatan Penduduk', 'Jumlah Penduduk', 'Jumlah Kasus TB',
            'rasio Pasien dan Jumlah Penduduk/10000', 'Jumlah Kasus DM',
            'Prevalensi DM/1000', 'Rasio penduduk dengan Fasyankes'
        ]

    def train_models(self, survey_data: pd.DataFrame):
        # Prepare X and y for Random Forest
        X_rf = survey_data.drop(
            ['ID Kelurahan', 'Kelurahan', 'Kecamatan', 'Jumlah Kasus TB'], axis=1)
        y_rf = survey_data['Jumlah Kasus TB']

        # Train Random Forest model
        self.random_forest_model.fit(X_rf, y_rf)

        # Prepare X for KMeans clustering
        X_km = survey_data[self.cluster_features]

        # Scale X for KMeans
        scaler = StandardScaler()
        X_km_scaled = scaler.fit_transform(X_km)

        # Train KMeans model
        self.kmeans_model.fit(X_km_scaled)

        # Mark models as trained
        self.models_trained = True

        # Save trained models
        self.save_models()

    def save_models(self):
        # Save models using pickle
        model_files = {
            'random_forest_model': os.path.join(self.model_dir, 'random_forest_model.pkl'),
            'kmeans_model': os.path.join(self.model_dir, 'kmeans_model.pkl')
        }

        for model_name, model_obj in model_files.items():
            with open(model_obj, 'wb') as f:
                pickle.dump(getattr(self, model_name), f)

    def load_models(self):
        # Load models using pickle
        model_files = {
            'random_forest_model': os.path.join(self.model_dir, 'random_forest_model.pkl'),
            'kmeans_model': os.path.join(self.model_dir, 'kmeans_model.pkl')
        }

        for model_name, model_obj in model_files.items():
            if os.path.exists(model_obj):
                with open(model_obj, 'rb') as f:
                    setattr(self, model_name, pickle.load(f))
            else:
                logger.warning(
                    f"Model file {model_obj} not found. Retraining the model.")
                return False

        return True

    def model_trained(self):
        return self.models_trained

    def load_data(self, file_path):
        # Load data from Excel file
        data = pd.read_excel(file_path)
        return data

    def compute_vulnerability_scores(self, data):
        # Compute vulnerability scores
        for feature, weight in self.weights.items():
            if feature in data.columns:
                data[feature] = data[feature] * weight

        data['Vulnerability_Score'] = data[list(
            self.weights.keys())].sum(axis=1)

    def cluster_data(self, data):
        # Select subset of features for clustering
        X_cluster = data[self.cluster_features]

        # Scale X_cluster
        scaler = StandardScaler()
        X_cluster_scaled = scaler.fit_transform(X_cluster)

        # Predict clusters using KMeans model
        clusters = self.kmeans_model.predict(X_cluster_scaled)
        data['Cluster'] = clusters

        return data

    def merge_data(self, original_data, cluster_data):
        # Merge cluster data with original data
        merged_data = pd.merge(original_data, cluster_data[['ID Kelurahan', 'Cluster']],
                               on='ID Kelurahan', how='left')

        # Define vulnerability levels
        merged_data['Vulnerability_Level'] = pd.qcut(merged_data['Vulnerability_Score'], q=4, labels=[
            'Tidak Rentan', 'Cukup Rentan', 'Rentan', 'Sangat Rentan'])

        return merged_data

    def create_bulk(self, db: Session, data: pd.DataFrame):
        # Prepare data for bulk insertion
        data_list = []
        for _, row in data.iterrows():
            data_list.append(KerentananCreate(
                kelurahan=row['Kelurahan'],
                jumlah_kasus=row['Jumlah Kasus TB'],
                kategori_kerentanan=row['Vulnerability_Level']
            ))

        # Insert data into database
        db_objs = [Kerentanan(**obj.dict()) for obj in data_list]
        db.add_all(db_objs)
        db.commit()

    def get_all(self, db: Session):
        # Retrieve all records from the database
        return db.query(Kerentanan).all()

    def get_by_kelurahan_id(self, db: Session, kelurahan_id: int):
        # Retrieve a record by Kelurahan ID from the database
        return db.query(Kerentanan).filter(Kerentanan.id == kelurahan_id).first()
