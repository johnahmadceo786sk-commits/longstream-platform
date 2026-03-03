from fastapi import APIRouter, HTTPException
from app.database.models.video import Video
from app.dependencies import get_db
from sqlalchemy.orm import Session
from fastapi import Depends

router = APIRouter(prefix="/stream", tags=["Streaming"])

@router.get("/{video_id}")
def get_stream_url(video_id: int, db: Session = Depends(get_db)):
    video = db.query(Video).filter(Video.id == video_id).first()
    if not video or not video.hls_path:
        raise HTTPException(status_code=404, detail="Stream not ready")

    return {"hls_url": video.hls_path}