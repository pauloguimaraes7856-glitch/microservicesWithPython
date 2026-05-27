from app.database import SessionLocal, Base, engine
from app import models

Base.metadata.create_all(bind=engine)

db = SessionLocal()

users = [
    models.User(
        id="11111111-1111-1111-1111-111111111111",
        username="alice",
        email="alice@test.com",
        hashed_password="hashed_123",
        is_active=True
    ),
    models.User(
        id="22222222-2222-2222-2222-222222222222",
        username="bob",
        email="bob@test.com",
        hashed_password="hashed_123",
        is_active=True
    ),
]

db.add_all(users)
db.commit()
db.close()

print("Seed completed")