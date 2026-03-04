from fastapi import APIRouter

router = APIRouter()
from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
import os

from app.database.session import get_db
from app.database.models.video import Video
from app.security.auth import get_current_host
from app.workers.tasks import process_video

router = APIRouter()

@router.post("/upload")
async def upload_video(file: UploadFile = File(...), db: Session = Depends(get_db), current_host=Depends(get_current_host)):
    # Save the uploaded file to a temporary location
    temp_file_path = f"/tmp/{file.filename}"
    with open(temp_file_path, "wb") as buffer:
        buffer.write(await file.read())

    # Create a new video record in the database
    new_video = Video(
        filename=file.filename,
        host_id=current_host.id,
        status="UPLOADED"
    )
    db.add(new_video)
    db.commit()
    db.refresh(new_video)

    # Enqueue the video processing task
    process_video.delay(new_video.id, temp_file_path)

    return {"message": "Video uploaded successfully", "video_id": new_video.id}
