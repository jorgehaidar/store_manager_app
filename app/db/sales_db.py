from app.db.database import Base
from sqlalchemy import ForeignKey, Column, Integer, DateTime
from datetime import datetime


class Sales(Base):
    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_item = Column(Integer, ForeignKey('item.id'), nullable=False)
    id_client = Column(Integer, ForeignKey('client.id'), nullable=False)
    amount = Column(Integer)
    sale_date = Column(DateTime(), default=datetime.now())

    def __str__(self):
        return f'id: {self.id}, ' \
               f'id_item: {self.id_item}, ' \
               f'id_client: {self.id_client}, ' \
               f'amount: {self.amount}, ' \
               f'sale_date: {self.sale_date}'
