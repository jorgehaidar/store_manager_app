from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DATE
from sqlalchemy.orm import Mapped, mapped_column, mapper, relationship
from app.db.database import Base
from app.schema.item_schema import ItemSchema


class Item(Base):
    __tablename__ = "item"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String)
    price: Mapped[float] = mapped_column(Float)
    purchase_price: Mapped[float] = mapped_column(Float)
    #purchase_date: Mapped[datetime] = mapped_column(DATE)
    tax: Mapped[float] = mapped_column(Float)
    location: Mapped[str] = mapped_column(String)
    #expiration_date: Mapped[datetime] = mapped_column(DATE)
    sale = relationship('Sale', uselist=False)

    # TODO: Add the column purchase_date
    # TODO: Add the column expiration_date
