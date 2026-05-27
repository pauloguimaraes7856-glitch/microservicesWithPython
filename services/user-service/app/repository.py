from app import models


def create_user(db, data, hashed_password: str):
    user = models.User(
        id=data.id,
        username=data.username,
        email=data.email,
        hashed_password=hashed_password,
        is_active=True
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user(db, user_id: str):
    return db.query(models.User).filter(models.User.id == user_id).first()


def list_users(db, limit: int = 100, offset: int = 0):
    query = db.query(models.User)
    total = query.count()
    users = query.offset(offset).limit(limit).all()
    return users, total
