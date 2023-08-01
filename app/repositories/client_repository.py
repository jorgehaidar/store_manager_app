from typing import List
from app.db.database import SessionLocal
from app.models.client import Client
from app.schema.client_schema import ClientSchema
from app.mappers.client_mapper import ClientMapper
from sqlalchemy.orm import Session

# TODO: change the input and output object to ItemSchema
class ClientRepository:
    def __init__(self, db: Session):
        self.db = db

    async def get_clients(self) -> List:
        return self.db.query(Client).all()

    def get_client_by_id(self, client_id: int):
        return self.db.query(Client).filter(Client.id == client_id).first()

    def create_client(self, client: Client):
        with SessionLocal() as session:
            session.add(client)
            session.commit()
            session.refresh(client)
            return client

    def update_client(self, client_id: int, client: ClientSchema):
        with SessionLocal() as session:
            """
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
            """
            # TODO: fix update_client functionality
            pass

    def delete_item(self, client_id: int) -> None:
        with SessionLocal() as session:
            session.query(Client).filter(Client.id == client_id).delete()
            session.commit()
