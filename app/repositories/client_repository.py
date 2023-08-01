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
        self.db.add(client)
        self.db.commit()
        self.db.refresh(client)
        return client

    def update_client(self, client_id: int, client: ClientSchema):
        db_client: Client = self.db.query(Client).filter(Client.id == client_id).first()

        if client.name != None:
            db_client.name = client.name

        if client.identity_card != None:
            db_client.identity_card = client.identity_card

        if client.phone != None:
            db_client.phone = client.phone

        if client.credit_card != None:
            db_client.credit_card = client.credit_card

        if client.debt != None:
            db_client.debt = client.debt

        self.db.commit()
        self.db.refresh(db_client)
        return db_client

    def delete_item(self, client_id: int) -> None:
        self.db.query(Client).filter(Client.id == client_id).delete()
        self.db.commit()
