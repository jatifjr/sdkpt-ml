import time
import requests
from typing import List, Optional, Union, Dict
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.semar_betul_auth import SemarBetulAuth
from app.models.patient import Patient
from app.schemas.semar_betul_auth import SemarBetulAuthBase, SemarBetulAuthCreate
from app.crud.patient import CRUDPatient  # Importing CRUDPatient class


class ApiClient:
    def __init__(self, base_url, db_session: Session):
        self.base_url = base_url
        self.db_session = db_session
        self.patient_crud = CRUDPatient()  # Initialize CRUDPatient instance

    def login(self, username, password):
        login_url = f"{self.base_url}/login"
        response = requests.post(
            login_url, data=SemarBetulAuthBase(username=username, password=password).dict())
        if response.status_code == 200:
            access_token = response.json()['access_token']
            auth_crud = CRUDBase(SemarBetulAuth)
            auth_obj = auth_crud.get(self.db_session, id="singleton")
            if auth_obj:
                auth_obj.access_token = access_token
                self.db_session.commit()
            else:
                auth_crud.create(self.db_session, obj_in=SemarBetulAuthCreate(
                    id="singleton", access_token=access_token).dict())
            return access_token
        else:
            print(f"Error fetching access token: {response.status_code}")
            return None

    def fetch_patient_data(self, access_token, page) -> Optional[Union[List[Patient], Dict[str, str]]]:
        patient_url = f"{self.base_url}/pasien?page={page}"
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(patient_url, headers=headers)

        # Print X-RateLimit-Remaining debug message
        remaining_requests = response.headers.get('X-RateLimit-Remaining')
        print(f"\033[93mDEBUG:\t\033[0mRemaining requests - {remaining_requests}")

        if response.status_code == 200:
            patient_data = response.json().get('data', [])

            if not patient_data:
                return {"detail": "All patient data already fetched.",
                        "status": "OK"}

            patients_to_insert = []
            duplicate_ids = []

            for patient_info in patient_data:
                patient_id = patient_info.get('id')
                existing_patient = self.db_session.query(
                    Patient).filter_by(id=patient_id).first()
                if existing_patient:
                    # Patient already exists, skip insertion
                    duplicate_ids.append(patient_id)
                else:
                    # Patient doesn't exist, so create a new Patient object
                    new_patient = Patient(
                        id=patient_id,
                        kelurahan_domisili=patient_info.get('kelurahan_domisili'),
                        kode_fasyankes=patient_info.get('kode_fasyankes'),
                        tahun=patient_info.get('tahun'),
                        bulan=patient_info.get('bulan'),
                        tipe_diagnosis=patient_info.get('tipe_diagnosis'),
                        anatomi_tb=patient_info.get('anatomi_tb'),
                        riwayat_hiv=patient_info.get('riwayat_hiv'),
                        riwayat_dm=patient_info.get('riwayat_dm'),
                        panduan_obat=patient_info.get('panduan_obat'),
                        sumber_obat=patient_info.get('sumber_obat'),
                        status_pengobatan=patient_info.get('status_pengobatan'),
                        pengobatan_terakhir=patient_info.get('pengobatan_terakhir')
                    )
                    patients_to_insert.append(new_patient)

            if patients_to_insert:
                self.db_session.add_all(patients_to_insert)
                self.db_session.commit()
                return patients_to_insert
            else:
                return {"detail": "All patient data already exists in the database.",
                        "duplicate_ids": duplicate_ids}
        else:
            print(f"Error fetching patient data: {response.status_code}")
            return None
