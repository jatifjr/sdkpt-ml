import os
from datetime import datetime
import pandas as pd
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends

router = APIRouter()

# Define the root directory of your project
PROJECT_ROOT = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))

# Directory for storing uploads
UPLOAD_DIR = os.path.join(PROJECT_ROOT, "uploads", "surveys")
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post('/upload-survey')
def upload_file(file: UploadFile = File(...)):
    # Check if a file was uploaded
    if not file:
        raise HTTPException(
            status_code=400, detail="No file uploaded. Please upload a file.")

    # Check the file extension
    if not file.filename.endswith('.xlsx'):
        raise HTTPException(
            status_code=400, detail="Invalid file type. Only .xlsx files are allowed.")

    try:
        # Generate a new filename using the current timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        new_filename = f"survey_{timestamp}.xlsx"
        file_location = os.path.join(UPLOAD_DIR, new_filename)

        # Save the file
        with open(file_location, "wb") as buffer:
            buffer.write(file.file.read())

        return {"message": "File uploaded successfully", "file_location": file_location}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        file.file.close()


@router.get('/process-survey')
def process_file(file_location: str):
    try:
        # Check if the file exists
        if not os.path.exists(file_location):
            raise HTTPException(status_code=404, detail="File not found.")

        # Read the Excel file using Pandas
        df = pd.read_excel(file_location)

        # Replace infinite values with NaN
        df.replace([float('inf'), float('-inf')], pd.NA, inplace=True)

        # Drop rows that are not fully filled
        df.dropna(inplace=True)

        # Convert data types where appropriate
        for col in df.columns:
            if col not in ['Kecamatan', 'Kelurahan', 'rasio Pasien dan Jumlah Penduduk/10000', 'Prevalensi DM/1000', 'Rasio penduduk dengan Fasyankes']:
                df[col] = pd.to_numeric(
                    df[col], errors='coerce').astype('Int64')

        # Fill remaining NaNs with None for JSON serialization
        df.fillna(value=None, inplace=True)

        # Convert DataFrame to JSON
        data = df.to_dict(orient='records')

        return {"data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
