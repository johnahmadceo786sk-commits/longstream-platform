from app.database.session import SessionLocal
from app.database.models.user import User
from app.security.hashing import hash_password

db = SessionLocal()

existing = db.query(User).filter(User.username == "john").first()

if not existing:
    user = User(
        username="john",
        hashed_password=hash_password("CEOjohn$$"),
        role="HOST"
    )
    db.add(user)
    db.commit()

print("Host initialized")