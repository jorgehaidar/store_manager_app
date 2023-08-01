from typing import List

from fastapi import APIRouter, Depends
from app.schema.client_schema import ClientSchema
from app.repositories.client_repository import ClientRepository
from app.services.client_service import ClientService
from app.db.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/clients")
async def read_clients(db: Session = Depends(get_db)):
    client_repository = ClientRepository(db)
    client_service = ClientService(client_repository)
    return await client_service.get_clients()


@router.get("/clients/{client_id}")
async def read_client(client_id: int, db: Session = Depends(get_db)):
    client_repository = ClientRepository(db)
    client_service = ClientService(client_repository)
    return client_service.get_client_by_id(client_id=client_id)


@router.post("/clients")
async def create_client(client: ClientSchema, db: Session = Depends(get_db)):
    client_repository = ClientRepository(db)
    client_service = ClientService(client_repository)
    return client_service.create_client(client=client)


@router.put("/clients/{client_id}", response_model=ClientSchema)
async def update_client(client_id: int, client: ClientSchema, client_repository: ClientRepository = Depends()):
    return client_repository.update_client(client_id=client_id, client=client)


@router.delete("/clients/{client_id}")
async def delete_client(client_id: int, client_repository: ClientRepository = Depends()):
    client_repository.delete_client(client_id=client_id)
    return {"message": "Client deleted successfully."}
