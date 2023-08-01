from app.schema.sale_schema import SaleSchema
from app.models.sale import Sale


class SaleMapper:

    @staticmethod
    def to_db(sale: SaleSchema) -> dict:
        return sale.dict()

    @staticmethod
    def to_entity(sale: Sale) -> SaleSchema:
        sale_dict = {
            'id': sale.id,
            'id_item': sale.id_item,
            'id_client': sale.id_client,
            'amount': sale.amount,
            'sale_date': sale.amount
        }
        return SaleSchema(**sale_dict)
