from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.database.models.video import Video

router = APIRouter(prefix="/search", tags=["Search"])

@router.get("/")
def search_videos(query: str, db: Session = Depends(get_db)):
    return db.query(Video).filter(Video.title.ilike(f"%{query}%")).all()