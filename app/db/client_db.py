from app.db.database import Base
from sqlalchemy import Column, Integer, String


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
