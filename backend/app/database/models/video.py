from sqlalchemy import Column, Integer, String, Text, BigInteger, DateTime, ForeignKey
from datetime import datetime

from app.database.base import Base


class Video(Base):

    __tablename__ = "videos"

    id = Column(Integer, primary_key=True)

    title = Column(String(255), nullable=False)
    description = Column(Text)

    stored_name = Column(String(255), nullable=False)

    duration = Column(Integer)
    size = Column(BigInteger)

    hls_path = Column(String(500))

    uploaded_by = Column(Integer, ForeignKey("users.id"))

    created_at = Column(DateTime, default=datetime.utcnow)