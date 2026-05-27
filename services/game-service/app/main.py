from fastapi import FastAPI

from app.routes import router
from app.database import engine, Base
from app.models import Game

Base.metadata.create_all(bind=engine)

app = FastAPI(title="game-service")

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(router)