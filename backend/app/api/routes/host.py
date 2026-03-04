from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db

router = APIRouter()

@router.post("/upload")
async def upload_video(
    title: str,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    return {"message": "Upload endpoint working"}