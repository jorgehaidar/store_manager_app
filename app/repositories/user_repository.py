from typing import List
from app.models.user import User
from sqlalchemy.orm import Session


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    async def get_users(self) -> List[User]:
        return self.db.query(User).all()

    def get_user_by_id(self, user_id: int) -> User:
        return self.db.query(User).filter(User.id == user_id).first()

    def create_user(self, user: User) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def update_user(self, user_id: int, user: User) -> User:
        db_user: User = self.db.query(User).filter(User.id == user_id).first()

        if user.email != None:
            db_user.email = user.email

        if user.password != None:
            db_user.password = user.password

        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def delete_user(self, user_id: int):
        delete = self.db.query(User).filter(User.id == user_id).delete()
        self.db.commit()
        return delete
