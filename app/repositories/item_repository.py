from typing import List
from app.db.database import SessionLocal
from app.models.item import Item
from app.schema.item_schema import ItemSchema
from app.mappers.item_mapper import ItemMapper


class ItemRepository:
    async def get_items(self) -> List:
        with SessionLocal() as session:
            return session.query(Item).all()

    def get_item_by_id(self, item_id: int):
        with SessionLocal() as session:
            return session.query(Item).filter(Item.id == item_id).first()

    def create_item(self, item: ItemSchema):
        with SessionLocal() as session:
            db_item = Item(**ItemMapper.to_db(item))
            session.add(db_item)
            session.commit()
            session.refresh(db_item)
            return db_item

    def update_item(self, item_id: int, item: ItemSchema):
        with SessionLocal() as session:
            db_item: Item = session.query(Item).filter(Item.id == item_id).first()
            db_item.name = item.name
            db_item.price = item.price
            db_item.purchase_price = item.purchase_price
            db_item.purchase_date = item.purchase_date
            db_item.tax = item.tax
            db_item.location = item.location
            db_item.expiration_date = item.expiration_date
            session.commit()
            session.refresh(db_item)
            return db_item

    def delete_item(self, item_id: int) -> None:
        with SessionLocal() as session:
            session.query(Item).filter(Item.id == item_id).delete()
            session.commit()
