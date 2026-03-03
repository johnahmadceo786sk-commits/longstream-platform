from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.database.models.video import Video
from app.database.models.download import Download

router = APIRouter(prefix="/download", tags=["Download"])

@router.get("/{video_id}")
def download_video(video_id: int, request: Request, db: Session = Depends(get_db)):
    video = db.query(Video).filter(Video.id == video_id).first()
    if not video:
        return {"error": "Video not found"}

    download = Download(
        video_id=video.id,
        ip_address=request.client.host
    )
    db.add(download)
    db.commit()

    return {"download_file": video.stored_name}