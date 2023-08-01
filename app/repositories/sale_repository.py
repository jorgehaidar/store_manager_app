from typing import List
from app.db.database import SessionLocal
from app.models.sale import Sale
from app.schema.sale_schema import SaleSchema
from app.mappers.sale_mapper import SaleMapper
from sqlalchemy.orm import Session


# TODO: change the input and output object to ItemSchema
class SaleRepository:
    def __init__(self, db: Session):
        self.db = db

    async def get_sales(self) -> List:
        return self.db.query(Sale).all()

    def get_sale_by_id(self, sale_id: int):
        return self.db.query(Sale).filter(Sale.id == sale_id).first()

    def create_sale(self, sale: Sale):
        self.db.add(sale)
        self.db.commit()
        self.db.refresh(sale)
        return sale

    def update_sale(self, sale_id: int, sale: Sale):
        db_sale: Sale = self.db.query(Sale).filter(Sale.id == sale_id).first()

        if sale.id_item != None:
            db_sale.id_item = sale.id_item

        if sale.id_client != None:
            db_sale.id_client = sale.id_client

        if sale.amount != None:
            db_sale.amount = sale.amount

        if sale.sale_date != None:
            db_sale.sale_date = sale.sale_date

        self.db.commit()
        self.db.refresh(db_sale)
        return db_sale

    def delete_sale(self, sale_id: int) -> None:
        self.db.query(Sale).filter(Sale.id == sale_id).delete()
        self.db.commit()
