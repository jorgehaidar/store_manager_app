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


# @router.get("/items/{item_id}", response_model=ItemSchema)
# async def read_item(item_id: int, item_repository: ItemRepository = Depends()):
#     return item_repository.get_item_by_id(item_id=item_id)
#
#
# @router.post("/items", response_model=ItemSchema)
# async def create_item(item: ItemSchema, item_repository: ItemRepository = Depends()):
#     return item_repository.create_item(item=item)
#
#
# @router.put("/items/{item_id}", response_model=ItemSchema)
# async def update_item(item_id: int, item: ItemSchema, item_repository: ItemRepository = Depends()):
#     return item_repository.update_item(item_id=item_id, item=item)
#
#
# @router.delete("/items/{item_id}")
# async def delete_item(item_id: int, item_repository: ItemRepository = Depends()):
#     item_repository.delete_item(item_id=item_id)
#     return {"message": "Item deleted successfully."}
