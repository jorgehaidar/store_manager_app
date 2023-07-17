from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, Date
from app.db.database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)
    purchase_price = Column(Float)
    purchase_date = Column(Date)
    tax = Column(Float)
    location = Column(String)
    expiration_date = Column(Date)
