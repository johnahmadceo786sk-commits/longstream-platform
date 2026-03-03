from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.sql import func
from app.database.base import Base

class Download(Base):
    __tablename__ = "downloads"

    id = Column(Integer, primary_key=True)
    video_id = Column(Integer, ForeignKey("videos.id"))
    ip_address = Column(String)
    downloaded_at = Column(DateTime(timezone=True), server_default=func.now())