from typing import List

from app.models.item import Item
from app.schema.item_schema import ItemSchema
from app.repositories.item_repository import ItemRepository


class ItemService:

    def __init__(self, item_repository: ItemRepository):
        self.item_repository = item_repository

    def get_items(self) -> List[ItemSchema]:
        return self.item_repository.get_items()

    def get_item_by_id(self, item_id: int) -> ItemSchema:
        return self.item_repository.get_item_by_id(item_id)

    def create_item(self, item: ItemSchema) -> Item:
        return self.item_repository.create_item(item)

    def update_item(self, item_id: int, item: ItemSchema) -> Item:
        return self.item_repository.update_item(item_id, item)

    def delete_item(self, item_id: int) -> None:
        return self.item_repository.delete_item(item_id)
