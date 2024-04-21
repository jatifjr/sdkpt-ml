import pandas as pd


class CaseService:
    def __init__(self):
        self.intervensi_static_df = pd.read_csv(
            "app/data/intervensi_static.csv")

    def get_cases_by_id(self, kelurahan_id):
        filtered_intervensi = self.intervensi_static_df[self.intervensi_static_df['id'] == kelurahan_id]

        # Check if the kelurahan_id exists
        if filtered_intervensi.empty:
            return {'error': 'Kelurahan not found'}

        case_column = 'Jumlah Kasus Aktif TB 2023'

        # Extract the active case value
        active_case = filtered_intervensi[case_column].values[0]

        # Convert the active case value to a JSON serializable type
        active_case_json_serializable = int(
            active_case) if not pd.isna(active_case) else None

        # Return a dictionary
        result = {'jumlah_kasus': active_case_json_serializable}

        return result
