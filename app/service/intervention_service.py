import pandas as pd
from fastapi import HTTPException


class IntervensiService:
    def __init__(self):
        self.kerentanan_df = pd.read_csv("app/data/kerentanan.csv")
        self.intervensi_df = pd.read_csv("app/data/intervensi.csv")
        self.intervensi_static_df = pd.read_csv(
            "app/data/intervensi_static.csv")

    def get_intervention_by_id(self, kelurahan_id):
        kerentanan_row = self.kerentanan_df[self.kerentanan_df['id']
                                            == kelurahan_id]

        if kerentanan_row.empty:
            return []

        kategori_kerentanan = kerentanan_row['kategori_kerentanan'].values[0]

        level_mapping = {
            "Tidak Rentan": 1,
            "Rentan": 2,
            "Cukup Rentan": 3,
            "Sangat Rentan": 4
        }

        level = level_mapping.get(kategori_kerentanan)

        filtered_intervensi = self.intervensi_df[self.intervensi_df['level_intervensi'] == level]
        # Return a list of dictionaries including both 'judul_intervensi' and 'isi_intervensi'
        result = [{'judul_intervensi': row['judul_intervensi'], 'isi_intervensi': row['isi_intervensi']}
                  for _, row in filtered_intervensi.iterrows()]

        # Return a list of dictionaries
        return result

    def get_interventions_list(self, kelurahan_id):
        # Check if the kelurahan_id is in the dataset
        if kelurahan_id not in self.intervensi_static_df['id'].values:
            raise HTTPException(
                status_code=404, detail="Kelurahan not found in the dataset")

        filtered_intervensi = self.intervensi_static_df[self.intervensi_static_df['id'] == kelurahan_id]

        # Extract interventions from 'Intervensi 1' to 'Intervensi 7'
        interventions_columns = ['Intervensi 1', 'Intervensi 2', 'Intervensi 3',
                                 'Intervensi 4', 'Intervensi 5', 'Intervensi 6', 'Intervensi 7']

        # Check if any value is "Undefined"
        if any(filtered_intervensi[column].values[0] == "Undefined" for column in interventions_columns):
            raise HTTPException(
                status_code=404, detail="Tidak ad intervensi")

        # If not, proceed to create the response
        interventions_list = []

        for _, row in filtered_intervensi.iterrows():
            for column in interventions_columns:
                intervention_dict = {
                    "isi_intervensi": row[column]
                }
                interventions_list.append(intervention_dict)

        return interventions_list
