from app.db.database import Base
from sqlalchemy import Column, Integer, Float, String, DateTime


class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    price = Column(Float)
    purchase_price = Column(Float, nullable=False)
    purchase_date = Column(DateTime)
    tax = Column(Float)
    location = Column(String(100))
    expiration_date = Column(DateTime)

    def __str__(self):
        return f'id: {self.id}, ' \
               f'name: {self.name}, ' \
               f'price: {self.price}, ' \
               f'purchase_price: {self.purchase_price}, ' \
               f'purchase_date: {self.purchase_date}, ' \
               f'tax: {self.tax}, ' \
               f'location = {self.location}, ' \
               f'expiration_date: {self.expiration_date}'
