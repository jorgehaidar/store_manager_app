import datetime

from sqlalchemy import Column, Integer, String, Float, DATETIME
from sqlalchemy.orm import Mapped, mapped_column, mapper
from app.db.database import Base


class Sale(Base):
    __tablename__ = "sale"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    id_item: Mapped[int] = mapped_column(Integer)
    id_client: Mapped[int] = mapped_column(Integer)
    amount: Mapped[int] = mapped_column(Integer)
    sale_date: Mapped[datetime] = mapped_column(DATETIME)

    # TODO: Add relation to table client
    # TODO: Add relation to table item

