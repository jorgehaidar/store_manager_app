from typing import List

from app.models.client import Client
from app.schema.client_schema import ClientSchema
from app.repositories.client_repository import ClientRepository
from app.mappers.client_mapper import ClientMapper


class ClientService:

    def __init__(self, client_repository: ClientRepository):
        self.client_repository = client_repository

    def get_clients(self) -> List[ClientSchema]:
        return self.client_repository.get_clients()

    def get_client_by_id(self, client_id: int) -> ClientSchema:
        return self.client_repository.get_client_by_id(client_id)

    def create_client(self, client: ClientSchema) -> Client:
        client_db = Client(**ClientMapper.to_db(client))
        return self.client_repository.create_client(client_db)

    def update_client(self, client_id: int, client: ClientSchema) -> Client:
        return self.client_repository.update_client(client_id, client)

    def delete_client(self, client_id: int) -> None:
        return self.client_repository.delete_client(client_id)
