from typing import List

from fastapi import APIRouter, Depends
from app.schema.item_schema import ItemSchema
from app.repositories.item_repository import ItemRepository
from app.services.item_service import ItemService
from sqlalchemy.orm import Session
from app.db.database import get_db

router = APIRouter()


@router.get("/items")
async def read_items(db: Session = Depends(get_db)):
    item_repository = ItemRepository(db)
    item_service = ItemService(item_repository)
    return await item_service.get_items()


@router.get("/items/{item_id}")
async def read_item(item_id: int, db: Session = Depends(get_db)):
    item_repository = ItemRepository(db)
    item_service = ItemService(item_repository)
    return item_service.get_item_by_id(item_id=item_id)


@router.post("/items")
async def create_item(item: ItemSchema, db: Session = Depends(get_db)):
    item_repository = ItemRepository(db)
    item_service = ItemService(item_repository)
    return item_service.create_item(item=item)


@router.put("/items/{item_id}")
async def update_item(item_id: int, item: ItemSchema, db: Session = Depends(get_db)):
    item_repository = ItemRepository(db)
    item_service = ItemService(item_repository)
    return item_service.update_item(item_id=item_id, item=item)


@router.delete("/items/{item_id}")
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    item_repository = ItemRepository(db)
    item_service = ItemService(item_repository)
    item_service.delete_item(item_id=item_id)
    return {"message": "Item deleted successfully."}
