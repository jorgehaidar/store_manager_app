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
        return self.db.query(Item).filter(Item.id == id).first()
        #with SessionLocal() as session:
        #    return session.query(Item).filter(Item.id == item_id).first()

    def create_item(self, item: ItemSchema):
        with SessionLocal() as session:
            item_db = Item(**ItemMapper.to_db(item))
            session.add(item_db)
            session.commit()
            session.refresh(item_db)
            return item

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
            # TODO: fix update_client functionality
            session.commit()
            session.refresh(db_item)
            return item

    def delete_item(self, item_id: int) -> None:
        with SessionLocal() as session:
            session.query(Item).filter(Item.id == item_id).delete()
            session.commit()
