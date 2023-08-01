from typing import List
from app.db.database import SessionLocal
from app.models.item import Item
from app.schema.item_schema import ItemSchema
from app.mappers.item_mapper import ItemMapper
from sqlalchemy.orm import Session


class ItemRepository:
    def __init__(self, db: Session):
        self.db = db

    async def get_items(self) -> List:
        return self.db.query(Item).all()
        #with SessionLocal() as session:
        #    return session.query(Item).all()

    def get_item_by_id(self, item_id: int):
        return self.db.query(Item).filter(Item.id == item_id).first()

    def create_item(self, item: ItemSchema):
        #TODO: arreglar el atributo que recibe ItemSchema -> Item
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item
        # with SessionLocal() as session:
        #     item_db = Item(**ItemMapper.to_db(item))
        #     session.add(item_db)
        #     session.commit()
        #     session.refresh(item_db)
        #     return item

    def update_item(self, item_id: int, item: Item):
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

    def delete_item(self, item_id: int) -> None:
        self.db.query(Item).filter(Item.id == item_id).delete()
        self.db.commit()
        # with SessionLocal() as session:
        #     session.query(Item).filter(Item.id == item_id).delete()
        #     session.commit()
