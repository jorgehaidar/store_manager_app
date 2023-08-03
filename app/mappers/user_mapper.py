from app.models.user import User
from app.schema.user_schema import UserSchema


class UserMapper:

    @staticmethod
    def to_db(user: UserSchema) -> dict:
        return user.dict()

    @staticmethod
    def to_entity(user: User) -> UserSchema:
        user_dict = {
            'id': user.id,
            'email': user.email,
            'name': user.name,
            'password': user.password,
        }
        return UserSchema(**user_dict)

