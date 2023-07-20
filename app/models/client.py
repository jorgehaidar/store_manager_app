from sqlalchemy import Column, Integer, String, Float, DATE
from sqlalchemy.orm import Mapped, mapped_column, mapper
from app.db.database import Base


class Client(Base):
    __tablename__ = "client"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String)
    identity_card: Mapped[str] = mapped_column(String)
    phone: Mapped[str] = mapped_column(String)
    credit_card: Mapped[str] = mapped_column(String)
    debt: Mapped[float] = mapped_column(Float)

