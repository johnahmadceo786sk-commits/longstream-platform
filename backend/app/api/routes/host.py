from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.database.models.video import Video

router = APIRouter(prefix="/host", tags=["Host"])


@router.post("/upload")
async def upload_video(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file uploaded")

    video = Video(
        title=file.filename,
        status="uploaded"
    )

    db.add(video)
    db.commit()
    db.refresh(video)

    return {
        "message": "Video uploaded successfully",
        "video_id": video.id
    }