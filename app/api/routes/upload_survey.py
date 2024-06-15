import os
from datetime import datetime
import pandas as pd
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import Session
from app.api import deps
from app.crud.upload_survey import upload_survey as survey
from app.crud.kerentanan import VulnerabilityService
from app.crud.intervention import InterventionService

router = APIRouter()
vulnerability_service = VulnerabilityService()
intervention_service = InterventionService()

# Define the root directory of your project
PROJECT_ROOT = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))

# Directory for storing uploads
UPLOAD_DIR = os.path.join(PROJECT_ROOT, "uploads", "surveys")
os.makedirs(UPLOAD_DIR, exist_ok=True)

# ! DO NOT TOUCH THIS


@router.post('/upload-survey')
async def upload_file(
    db: Session = Depends(deps.get_db),
    file: UploadFile = File(...)
):
    # Check if a file was uploaded
    if not file:
        raise HTTPException(
            status_code=400, detail="No file uploaded. Please upload a file."
        )

    # Check the file extension
    if not file.filename.endswith('.xlsx'):
        raise HTTPException(
            status_code=400, detail="Invalid file type. Only .xlsx files are allowed."
        )

    try:
        # Generate a new filename using the current timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        new_filename = f"survey_{timestamp}.xlsx"
        file_location = os.path.join(UPLOAD_DIR, new_filename)

        # Save the file
        with open(file_location, "wb") as buffer:
            buffer.write(await file.read())

        # Load data from Excel file
        data = vulnerability_service.load_data(file_location)

        intervention_service.compute_and_update_interventions(
            db, file_location)

        # # Compute intervention scores
        # print(data.columns.to_list())
        # tfidf_data = intervention_service.calculate_tfidf(data)
        # print(tfidf_data)
        # weighted_data = intervention_service.apply_weights(tfidf_data)
        # print(weighted_data)
        # ranked_data = intervention_service.rank_categories(weighted_data)

        # print(data.columns)

        # # Train models if not already trained
        # if not vulnerability_service.model_trained():
        #     vulnerability_service.train_models(data)
        # else:
        #     # Load existing models
        #     vulnerability_service.load_models()

        # Compute vulnerability scores
        vulnerability_data = vulnerability_service.compute_vulnerability_scores(
            data)

        # print(vulnerability_data.columns)

        # Merge data with original data
        merged_data = vulnerability_service.merge_data(
            data, vulnerability_data)

        # print(merged_data.columns)

        # Create records in database
        vulnerability_service.create_bulk(db, merged_data)

        # ranked_categories, interventions = intervention_service.get_ranked_interventions(
        #     file_location)
        # intervention_service.save_interventions_to_database(db, file_location)
        # intervention_service.save_interventions_to_database(db, ranked_data)

        return {"message": f"Survey data uploaded and processed successfully"}

    # except Exception as e:
    #     raise HTTPException(status_code=500, detail=str(e))

    finally:
        await file.close()
