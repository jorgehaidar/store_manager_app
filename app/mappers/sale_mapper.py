from app.schema.sale_schema import SaleSchema


class SaleMapper:

    @staticmethod
    def to_db(sale: SaleSchema) -> dict:
        return sale.dict()

    @staticmethod
    def to_entity(sale: dict) -> SaleSchema:
        return SaleSchema(**sale)
