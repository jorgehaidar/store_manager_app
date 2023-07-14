import json

from sqlalchemy import insert
from app.models.item import Item
from app.db.database import SessionLocal, engine

session = SessionLocal()


class ItemService:

    def index(self):
        return session.query(Item).all()

    def store(self, item: Item):
        stmt = insert(item).values(name=f'{item.name}',
                                   price=f'{item.price}',
                                   purchase_price=f'{item.purchase_price}',
                                   purchase_date=f'{item.purchase_date}',
                                   tax=f'{item.tax}',
                                   location=f'{item.location}',
                                   expiration_date=f'{item.expiration_date}')
        with engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
    def show(self, item: Item):
        pass

    def update(self, request, item: Item):
        pass

    def delete(self, id):
        pass
