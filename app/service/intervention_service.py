import pandas as pd


class IntervensiService:
    def __init__(self):
        self.kerentanan_df = pd.read_csv("app/data/kerentanan.csv")
        self.intervensi_df = pd.read_csv("app/data/intervensi.csv")

    def get_intervention_by_id(self, kelurahan_id):
        kerentanan_row = self.kerentanan_df[self.kerentanan_df['id']
                                            == kelurahan_id]

        if kerentanan_row.empty:
            return "Kelurahan not found"

        kategori_kerentanan = kerentanan_row['kategori_kerentanan'].values[0]

        level_mapping = {
            "Tidak Rentan": 1,
            "Rentan": 2,
            "Cukup Rentan": 3,
            "Sangat Rentan": 4
        }

        level = level_mapping.get(kategori_kerentanan)

        filtered_intervensi = self.intervensi_df[self.intervensi_df['level_intervensi'] == level]
        unique_tipe_intervensi = filtered_intervensi['tipe_intervensi'].unique(
        )

        isi_intervensi = filtered_intervensi['isi_intervensi'].tolist()

        return isi_intervensi
