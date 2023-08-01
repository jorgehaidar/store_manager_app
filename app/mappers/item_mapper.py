from app.models.item import Item
from app.schema.item_schema import ItemSchema


class ItemMapper:

    @staticmethod
    def to_db(item: ItemSchema) -> dict:
        return item.dict()

    @staticmethod
    def to_entity(item: Item) -> ItemSchema:
        item_dict = {
            'id': item.id,
            'name': item.name,
            'price': item.price,
            'purchase_price': item.purchase_price,
            'tax': item.tax,
            'location': item.location
        }
        return ItemSchema(**item_dict)

