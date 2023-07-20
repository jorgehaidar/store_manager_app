from typing import List

from app.models.sale import Sale
from app.schema.sale_schema import SaleSchema
from app.repositories.sale_repository import SaleRepository
from app.mappers.sale_mapper import SaleMapper


class SaleService:

    def __init__(self, sale_repository: SaleRepository):
        self.sale_repository = sale_repository

    def get_sales(self) -> List[SaleSchema]:
        return self.sale_repository.get_sales()

    def get_sale_by_id(self, sale_id: int) -> SaleSchema:
        return self.sale_repository.get_sale_by_id(sale_id)

    def create_sale(self, sale: SaleSchema) -> Sale:
        sale_db = sale(**SaleMapper.to_db(sale))
        return self.sale_repository.create_sale(sale_db)

    def update_sale(self, sale_id: int, sale: SaleSchema) -> Sale:
        return self.sale_repository.update_sale(sale_id, sale)

    def delete_sale(self, sale_id: int) -> None:
        return self.sale_repository.delete_sale(sale_id)
