from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db

router = APIRouter()


@router.post("/login")
def login():
    return {"message": "Login endpoint"}