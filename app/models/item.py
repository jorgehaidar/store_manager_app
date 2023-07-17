from datetime import date
from pydantic import BaseModel


class Item(BaseModel):
    id: int
    name: str
    price: float
    purchase_price: float
    purchase_date: date
    tax: float
    location: str
    expiration_date: date

