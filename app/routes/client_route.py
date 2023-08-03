from typing import List

from fastapi import APIRouter, Depends, HTTPException
from app.schema.client_schema import ClientSchema
from app.repositories.client_repository import ClientRepository
from app.services.client_service import ClientService
from app.db.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/clients',
    tags=['clients']
)


@router.get("/")
async def read_clients(db: Session = Depends(get_db)):
    client_repository = ClientRepository(db)
    client_service = ClientService(client_repository)
    return await client_service.get_clients()


@router.get("/{client_id}")
async def read_client(client_id: int, db: Session = Depends(get_db)):
    client_repository = ClientRepository(db)
    client_service = ClientService(client_repository)
    client = client_service.get_client_by_id(client_id=client_id)
    if client is None:
        raise HTTPException(
            status_code=404,
            detail='Client not found'
        )
    return client

#TODO: El estado de respuesta de creado debe ser 201
@router.post("/")
async def create_client(client: ClientSchema, db: Session = Depends(get_db)):
    client_repository = ClientRepository(db)
    client_service = ClientService(client_repository)
    return client_service.create_client(client=client)


@router.put("/{client_id}", response_model=ClientSchema)
async def update_client(client_id: int, client: ClientSchema, db: Session = Depends(get_db)):
    client_repository = ClientRepository(db)
    client_service = ClientService(client_repository)
    return client_service.update_client(client_id=client_id, client=client)


@router.delete("/{client_id}")
async def delete_client(client_id: int, db: Session = Depends(get_db)):
    client_repository = ClientRepository(db)
    client_service = ClientService(client_repository)
    client_service.delete_client(client_id=client_id)
    return {"message": "Client deleted successfully."}
