from typing import List

from fastapi import APIRouter, Depends

from app.db.database import SessionLocal
from app.models.item import Item
from app.repositories.item_repository import ItemRepository

router = APIRouter()


@router.get("/items", response_model=List[Item])
async def read_items(item_repository: ItemRepository = Depends()):
    return await item_repository.get_items()


@router.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int, item_repository: ItemRepository = Depends()):
    return await item_repository.get_item_by_id(item_id=item_id)


@router.post("/items", response_model=Item)
async def create_item(item: Item, item_repository: ItemRepository = Depends()):
    return await item_repository.create_item(item=item)


@router.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item, item_repository: ItemRepository = Depends()):
    return await item_repository.update_item(item_id=item_id, item=item)


@router.delete("/items/{item_id}")
async def delete_item(item_id: int, item_repository: ItemRepository = Depends()):
    await item_repository.delete_item(item_id=item_id)
    return {"message": "Item deleted successfully."}
