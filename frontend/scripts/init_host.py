from datetime import datetime
from app.database.session import SessionLocal
from app.database.models.user import User
from app.security.hashing import hash_password

db = SessionLocal()

host = User(
    username="john",
    hashed_password=hash_password("CEOjohn$$"),
    role="HOST",
    created_at=datetime.utcnow()
)

db.add(host)
db.commit()

print("Host user created")