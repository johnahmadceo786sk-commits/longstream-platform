from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.database.models.video import Video

router = APIRouter(prefix="/videos", tags=["Public"])

@router.get("/")
def list_videos(db: Session = Depends(get_db)):
    return db.query(Video).all()

@router.get("/{video_id}")
def get_video(video_id: int, db: Session = Depends(get_db)):
    return db.query(Video).filter(Video.id == video_id).first()