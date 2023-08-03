from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column, mapper, relationship
from app.db.database import Base


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String)

