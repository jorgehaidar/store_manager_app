from app.models.item import Item
from app.schema.item_schema import ItemSchema


class ItemMapper:

    @staticmethod
    def to_db(item: ItemSchema) -> dict:
        return item.dict()

    @staticmethod
    def to_entity(item: dict) -> ItemSchema:
        return ItemSchema(**item)
