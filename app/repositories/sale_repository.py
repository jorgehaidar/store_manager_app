from typing import List
from app.db.database import SessionLocal
from app.models.sale import Sale
from app.schema.sale_schema import SaleSchema
from app.mappers.sale_mapper import SaleMapper


# TODO: change the input and output object to ItemSchema
class SaleRepository:
    async def get_sales(self) -> List:
        with SessionLocal() as session:
            return session.query(Sale).all()

    def get_sale_by_id(self, sale_id: int):
        with SessionLocal() as session:
            return session.query(Sale).filter(Sale.id == sale_id).first()

    def create_sale(self, sale: Sale):
        with SessionLocal() as session:
            session.add(sale)
            session.commit()
            session.refresh(sale)
            return sale

    def update_sale(self, sale_id: int, sale: SaleSchema):
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

    def delete_sale(self, sale_id: int) -> None:
        with SessionLocal() as session:
            session.query(Sale).filter(Sale.id == sale_id).delete()
            session.commit()
