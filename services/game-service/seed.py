from app.database import SessionLocal, Base, engine
from app import models

Base.metadata.create_all(bind=engine)

db = SessionLocal()

games = [
    models.Game(
        title="Zelda Breath of the Wild",
        genre="adventure",
        platform="Switch",
        cover_url="https://example.com/zelda.jpg"
    ),
    models.Game(
        title="FIFA 24",
        genre="sports",
        platform="PS5",
        cover_url="https://example.com/fifa.jpg"
    ),
]

db.add_all(games)
db.commit()
db.close()

print("Game seed completed")