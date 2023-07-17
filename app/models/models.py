from app.db.database import Base
from sqlalchemy import Column, Integer, String, Float, DATETIME, ForeignKey
from sqlalchemy.orm import relationship


class Client(Base):
    __tablename__ = 'client'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    identity_card = Column(Integer)
    phone = Column(String(32))
    credit_card = Column(Integer)
    debt = Column(Integer)

    def __str__(self):
        return f'id: {self.id}, ' \
               f'name: {self.name}, ' \
               f'identity_card: {self.identity_card}, ' \
               f'phone: {self.phone}, ' \
               f'credit_card: {self.credit_card}, ' \
               f'debt: {self.debt}'



class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    price = Column(Float)
    purchase_price = Column(Float, nullable=False)
    purchase_date = Column(DATETIME)
    tax = Column(Float)
    location = Column(String(100))
    expiration_date = Column(DATETIME)

    def __str__(self):
        return f'id: {self.id}, ' \
               f'name: {self.name}, ' \
               f'price: {self.price}, ' \
               f'purchase_price: {self.purchase_price}, ' \
               f'purchase_date: {self.purchase_date}, ' \
               f'tax: {self.tax}, ' \
               f'location = {self.location}, ' \
               f'expiration_date: {self.expiration_date}'



class Sales(Base):
    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_item = Column(Integer, ForeignKey('item.id'), nullable=False)
    id_client = Column(Integer, ForeignKey('client.id'), nullable=False)
    amount = Column(Integer)
    sale_date = Column(DATETIME, default=DATETIME.now())

    def __str__(self):
        return f'id: {self.id}, ' \
               f'id_item: {self.id_item}, ' \
               f'id_client: {self.id_client}, ' \
               f'amount: {self.amount}, ' \
               f'sale_date: {self.sale_date}'
