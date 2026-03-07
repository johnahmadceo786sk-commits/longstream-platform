from sqlalchemy import Column, Integer, DateTime, ForeignKey
from datetime import datetime

from app.database.base import Base


class Download(Base):

    __tablename__ = "downloads"

    id = Column(Integer, primary_key=True)

    video_id = Column(Integer, ForeignKey("videos.id"))

    downloaded_at = Column(DateTime, default=datetime.utcnow)