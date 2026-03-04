from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
import os

from app.database.session import get_db
from app.database.models.video import Video
from app.security.auth import get_current_host
from app.workers.tasks import process_video

router = APIRouter()

