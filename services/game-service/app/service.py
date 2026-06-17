from sqlalchemy.orm import Session

from app import repository
from app.schemas import GameCreate, GameOut, GameList
from app.infrastructure.cache import set_game_summary


def add_game(db: Session, data: GameCreate) -> GameOut:
    game = repository.create_game(db, data)
    result = GameOut.model_validate(game)
    set_game_summary(result.id, {
        "id": result.id,
        "title": result.title,
        "genre": result.genre,
        "platform": result.platform,
        "cover_url": result.cover_url,
    })
    return result

def fetch_game(db: Session, game_id: str) -> GameOut:
    game = repository.get_game(db, game_id)
    if game is None:
        raise ValueError(f"Game {game_id} not found")
    return GameOut.model_validate(game)

def fetch_all_games(db: Session, limit: int = 20, offset: int = 0) -> GameList:
    games, total = repository.list_games(db, limit=limit, offset=offset)
    return GameList(
        items=[GameOut.model_validate(game) for game in games],
        total=total,
        limit=limit,
        offset=offset,
    )

def search_games(db: Session, q: str) -> list[GameOut]:
    games = repository.search_games(db, q)
    return [GameOut.model_validate(game) for game in games]

def remove_game(db: Session, game_id: str) -> None:
    deleted = repository.delete_game(db, game_id)
    if not deleted:
        raise ValueError(f"Game {game_id} not found")