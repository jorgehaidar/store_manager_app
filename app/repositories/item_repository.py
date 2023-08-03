from typing import List
from app.models.item import Item
from sqlalchemy.orm import Session


class ItemRepository:
    def __init__(self, db: Session):
        self.db = db

    async def get_items(self) -> List[Item]:
        return self.db.query(Item).all()

    def get_item_by_id(self, item_id: int) -> Item:
        return self.db.query(Item).filter(Item.id == item_id).first()

    def create_item(self, item: Item) -> Item:
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item

    def update_item(self, item_id: int, item: Item) -> Item:
        db_item: Item = self.db.query(Item).filter(Item.id == item_id).first()

        if item.name != None:
            db_item.name = item.name

        if item.price != None:
            db_item.price = item.price

        if item.purchase_price != None:
            db_item.purchase_price = item.purchase_price

        if item.tax != None:
            db_item.tax = item.tax

        if item.location != None:
            db_item.location = item.location

        self.db.commit()
        self.db.refresh(db_item)
        return db_item

    def delete_item(self, item_id: int):
        delete = self.db.query(Item).filter(Item.id == item_id).delete()
        self.db.commit()
        return delete
