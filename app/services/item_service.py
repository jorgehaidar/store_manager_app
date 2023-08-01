from typing import List

from app.models.item import Item
from app.schema.item_schema import ItemSchema
from app.repositories.item_repository import ItemRepository
from app.mappers.item_mapper import ItemMapper


class ItemService:

    def __init__(self, item_repository: ItemRepository):
        self.item_repository = item_repository

    def get_items(self) -> List[ItemSchema]:
        return self.item_repository.get_items()

    def get_item_by_id(self, item_id: int) -> ItemSchema:
        return self.item_repository.get_item_by_id(item_id)

    def create_item(self, item: ItemSchema) -> Item:
        item_db = Item(**ItemMapper.to_db(item))
        return self.item_repository.create_item(item_db)

    def update_item(self, item_id: int, item: ItemSchema) -> ItemSchema:
        db_item: Item = self.item_repository.update_item(item_id, item)
        return ItemMapper.to_entity(db_item)

    def delete_item(self, item_id: int) -> None:
        return self.item_repository.delete_item(item_id)
