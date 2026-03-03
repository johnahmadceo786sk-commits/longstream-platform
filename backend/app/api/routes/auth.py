from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.schemas.user_schema import UserLogin
from app.security.auth import login_user

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login(data: UserLogin, db: Session = Depends(get_db)):
    return login_user(data.username, data.password, db)