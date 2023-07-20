from app.models.client import Client
from app.schema.client_schema import ClientSchema


class ClientMapper:

    @staticmethod
    def to_db(client: ClientSchema) -> dict:
        return client.dict()

    @staticmethod
    def to_entity(client: dict) -> ClientSchema:
        return ClientSchema(**client)
