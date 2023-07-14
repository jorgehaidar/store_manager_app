from pydantic import BaseModel
from datetime import datetime


class Item(BaseModel):
    id: int
    name: str
    price: float
    purchase_price: float
    purchase_date: datetime
    tax: float
    location: str
    expiration_date: datetime
