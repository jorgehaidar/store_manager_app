from app.models.client import Client
from app.schema.client_schema import ClientSchema


class ClientMapper:

    @staticmethod
    def to_db(client: ClientSchema) -> dict:
        return client.dict()

    @staticmethod
    def to_entity(client: Client) -> ClientSchema:
        client_dict = {
            'id': client.id,
            'name': client.name,
            'identity_card': client.identity_card,
            'phone': client.phone,
            'credit_card': client.credit_card,
            'debt': client.debt
        }
        return ClientSchema(**client_dict)
