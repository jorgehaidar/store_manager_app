from typing import List

from fastapi import APIRouter, Depends, HTTPException
from app.schema.user_schema import UserSchema
from app.repositories.client_repository import ClientRepository
from app.services.client_service import ClientService
from app.models.user import User
from app.db.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.get("/")
async def read_users(db: Session = Depends(get_db)):
    # client_repository = ClientRepository(db)
    # client_service = ClientService(client_repository)
    # return await client_service.get_clients()
    pass


@router.get("/{user_id}")
async def read_user(user_id: int, db: Session = Depends(get_db)):
    # client_repository = ClientRepository(db)
    # client_service = ClientService(client_repository)
    # client = client_service.get_client_by_id(client_id=client_id)
    # if client is None:
    #     raise HTTPException(
    #         status_code=404,
    #         detail='Client not found'
    #     )
    # return client
    pass


@router.post("/")
async def create_user(user: UserSchema, db: Session = Depends(get_db)):
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # client_repository = ClientRepository(db)
    # client_service = ClientService(client_repository)
    # return client_service.create_client(client=client)
    pass


@router.put("/{user_id}", response_model=UserSchema)
async def update_client(user_id: int, user: UserSchema, db: Session = Depends(get_db)):
    # client_repository = ClientRepository(db)
    # client_service = ClientService(client_repository)
    # return client_service.update_client(client_id=client_id, client=client)
    pass


@router.delete("/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    # client_repository = ClientRepository(db)
    # client_service = ClientService(client_repository)
    # client_service.delete_client(client_id=client_id)
    # return {"message": "Client deleted successfully."}
    pass
