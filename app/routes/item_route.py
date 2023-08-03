from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from app.schema.item_schema import ItemSchema
from app.repositories.item_repository import ItemRepository
from app.services.item_service import ItemService
from sqlalchemy.orm import Session
from app.db.database import get_db

router = APIRouter(
    prefix='/items',
    tags=['items']
)


@router.get("/")
async def read_items(db: Session = Depends(get_db)):
    item_repository = ItemRepository(db)
    item_service = ItemService(item_repository)
    return await item_service.get_items()


@router.get("/{item_id}", status_code=status.HTTP_200_OK)
async def read_item(item_id: int, db: Session = Depends(get_db)):
    item_repository = ItemRepository(db)
    item_service = ItemService(item_repository)
    item = item_service.get_item_by_id(item_id=item_id)
    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Item not found'
        )
    return item

#TODO: El estado de respuesta de creado debe ser 201
@router.post("/")
async def create_item(item: ItemSchema, db: Session = Depends(get_db)):
    item_repository = ItemRepository(db)
    item_service = ItemService(item_repository)
    return item_service.create_item(item=item)


@router.put("/{item_id}")
async def update_item(item_id: int, item: ItemSchema, db: Session = Depends(get_db)):
    item_repository = ItemRepository(db)
    item_service = ItemService(item_repository)
    return item_service.update_item(item_id=item_id, item=item)


@router.delete("/{item_id}")
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    item_repository = ItemRepository(db)
    item_service = ItemService(item_repository)
    item = item_service.delete_item(item_id=item_id)
    if item:
        return {"message": "Item deleted successfully."}
    else:
        raise HTTPException(
            status_code=404,
            detail='Item not found'
        )

