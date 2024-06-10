import os
from datetime import datetime
import pandas as pd
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import Session
from app.api import deps
from app.crud.upload_survey import upload_survey as survey

router = APIRouter()

# Define the root directory of your project
PROJECT_ROOT = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))

# Directory for storing uploads
UPLOAD_DIR = os.path.join(PROJECT_ROOT, "uploads", "surveys")
os.makedirs(UPLOAD_DIR, exist_ok=True)

# ! DO NOT TOUCH THIS
@router.post('/upload-survey')
async def upload_file(db: Session = Depends(deps.get_db), file: UploadFile = File(...)):
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
            buffer.write(await file.read())

        created_surveys = survey.create_from_excel(db, file_location)
        return {"message": f"{len(created_surveys)} surveys created successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        await file.close()
