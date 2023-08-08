from typing import List

from fastapi import APIRouter, Depends, HTTPException
from app.schema.user_schema import UserSchema
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService
from app.models.user import User
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.schema import schema
from .. import oaut2

router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.get("/")
async def read_users(db: Session = Depends(get_db),
                     current_user: UserSchema = Depends(oaut2.get_current_user)):
    user_repository = UserRepository(db)
    user_service = UserService(user_repository)
    return await user_service.get_users()


@router.get("/{user_id}")
async def read_user(user_id: int,
                    db: Session = Depends(get_db),
                    current_user: UserSchema = Depends(oaut2.get_current_user)):
    user_repository = UserRepository(db)
    user_service = UserService(user_repository)
    user = user_service.get_user_by_id(user_id=user_id)
    if user is None:
        raise HTTPException(
            status_code=404,
            detail='user not found'
        )
    return user


@router.post("/", response_model=schema.ShowUser)
async def create_user(user: UserSchema,
                      db: Session = Depends(get_db),
                      current_user: UserSchema = Depends(oaut2.get_current_user)):
    user_repository = UserRepository(db)
    user_service = UserService(user_repository)
    return user_service.create_user(user=user)


@router.put("/{user_id}", response_model=schema.ShowUser)
async def update_user(user_id: int,
                      user: UserSchema,
                      db: Session = Depends(get_db),
                      current_user: UserSchema = Depends(oaut2.get_current_user)):
    user_repository = UserRepository(db)
    user_service = UserService(user_repository)
    return user_service.update_user(user_id=user_id, user=user)


@router.delete("/{user_id}")
async def delete_user(user_id: int,
                      db: Session = Depends(get_db),
                      current_user: UserSchema = Depends(oaut2.get_current_user)):
    user_repository = UserRepository(db)
    user_service = UserService(user_repository)
    user_service.delete_user(user_id=user_id)
    return {"message": "user deleted successfully."}
