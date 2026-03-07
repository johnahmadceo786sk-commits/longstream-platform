from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.database.base import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(String(50), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)