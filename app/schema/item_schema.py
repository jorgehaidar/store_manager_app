from datetime import date
from pydantic import BaseModel


class ItemSchema(BaseModel):
    id: int
    name: str
    price: float
    purchase_price: float
    #purchase_date: date
    tax: float
    location: str
    #expiration_date: date

    # TODO: Add the column purchase_date
    # TODO: Add the column purchase_date

    class Config:
        orm_mode = True

