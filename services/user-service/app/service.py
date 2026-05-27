import uuid
from app import repository, models
from app.schemas import UserOut, UserList


class UserService:

    def _hash_password(self, password: str) -> str:
        return f"hashed_{password}"

    def add_user(self, db, data):
        user = models.User(
            id=str(uuid.uuid4()),
            username=data.username,
            email=data.email,
            hashed_password=self._hash_password(data.password)
        )

        created = repository.create_user(
            db,
            data=user,
            hashed_password=user.hashed_password
        )

        return UserOut.model_validate(created)

    def fetch_user(self, db, user_id: str):
        user = repository.get_user(db, user_id)
        if not user:
            raise ValueError("User not found")
        return UserOut.model_validate(user)

    def fetch_all_users(self, db, limit: int, offset: int):
        users, total = repository.list_users(db, limit, offset)

        return UserList(
            items=[UserOut.model_validate(u) for u in users],
            total=total,
            limit=limit,
            offset=offset
        )