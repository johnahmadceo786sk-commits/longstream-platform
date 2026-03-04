from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
import os

from app.database.session import get_db
from app.database.models.video import Video
from app.core.security import get_current_host
from app.workers.tasks import process_video

router = APIRouter()

UPLOAD_DIR = "storage/raw"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_video(
    title: str,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    host=Depends(get_current_host)
):
    # Save file locally
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # Create DB record
    video = Video(
        title=title,
        original_filename=file.filename,
        stored_name=file.filename,
        uploaded_by=host.id
    )

    db.add(video)
    db.commit()
    db.refresh(video)

    # Trigger async processing
    process_video.delay(video.id, file_path)

    return {"message": "Upload successful", "video_id": video.id}