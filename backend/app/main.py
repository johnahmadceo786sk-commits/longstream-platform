from fastapi import FastAPI
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.database.models.user import User
from app.security.hashing import hash_password

# Import routers
from app.api.routes import auth, host, public, search, stream, download

app = FastAPI(title="LongStream Backend")

# Register routers
app.include_router(auth.router)
app.include_router(host.router)
app.include_router(public.router)
app.include_router(search.router)
app.include_router(stream.router)
app.include_router(download.router)


@app.on_event("startup")
def create_default_host():
    db: Session = next(get_db())
    try:
        existing = db.query(User).filter(User.username == "john").first()
        if not existing:
            default_user = User(
                username="john",
                hashed_password=hash_password("CEOjohn$$"),
                role="HOST"
            )
            db.add(default_user)
            db.commit()
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "LongStream Backend Running"}