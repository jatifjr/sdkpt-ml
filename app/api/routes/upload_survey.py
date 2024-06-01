import os
import logging
from datetime import datetime

from fastapi import APIRouter, UploadFile, File, HTTPException

router = APIRouter()

# Define the root directory of your project
PROJECT_ROOT = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))

# Directory for storing uploads
UPLOAD_DIR = os.path.join(PROJECT_ROOT, "uploads", "surveys")
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Set up logging
# logging.basicConfig(level=logging.DEBUG)


@router.post('/')
def upload_file(file: UploadFile = File(...)):
    # Check the file extension
    if not file.filename.endswith('.xlsx'):
        raise HTTPException(
            status_code=400, detail="Invalid file type. Only .xlsx files are allowed.")

    # Check the MIME type
    if file.content_type != 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
        raise HTTPException(
            status_code=400, detail="Invalid file type. Only .xlsx files are allowed.")

    try:
        # Generate a new filename using the current timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        new_filename = f"survey_{timestamp}.xlsx"
        file_location = os.path.join(UPLOAD_DIR, new_filename)
        # logging.debug(f"Saving file to: {file_location}")

        with open(file_location, "wb") as buffer:
            buffer.write(file.file.read())

        # Return a JSON response
        return {"message": "File uploaded successfully", "filename": file.filename}
    except Exception as e:
        # logging.error(f"Error uploading file: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        file.file.close()


# # Example of listing uploaded files
# uploaded_files = os.listdir(UPLOAD_DIR)
# print(f"Uploaded files in {UPLOAD_DIR}:")
# for file_name in uploaded_files:
#     print(file_name)
