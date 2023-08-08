from typing import List

from app.models.user import User
from app.schema.user_schema import UserSchema
from app.repositories.user_repository import UserRepository
from app.mappers.user_mapper import UserMapper
from app.hashing import Hash


class UserService:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_users(self):
        return self.user_repository.get_users()

    def get_user_by_id(self, user_id: int) -> UserSchema:
        return self.user_repository.get_user_by_id(user_id)

    def create_user(self, user: UserSchema) -> UserSchema:
        user.password = Hash.get_password_hash(user.password)
        user_db = User(**UserMapper.to_db(user))
        return self.user_repository.create_user(user_db)

    def update_user(self, user_id: int, user: UserSchema) -> UserSchema:
        user.password = Hash.get_password_hash(user.password)
        db_user: User = self.user_repository.update_user(user_id, user)
        return UserMapper.to_entity(db_user)

    def delete_user(self, user_id: int) -> None:
        return self.user_repository.delete_user(user_id)
