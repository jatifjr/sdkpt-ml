from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/")
async def root():
    try:
        content = {
            "message": "SDKPT Machine Learning API by Ahmad Fajar Kusumajati",
            "status": "ok"
        }
        headers = {
            "access_token": "none"
        }
        return JSONResponse(content=content, headers=headers)
    except:
        raise HTTPException(status_code=500, detail="Internal Server Error")
