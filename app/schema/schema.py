from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class ShowItem(BaseModel):
    name: str
    price: float
    purchase_price: float
    # purchase_date: date
    tax: float
    location: str
    # expiration_date: date

    class Config:
        orm_mode = True


class ShowClient(BaseModel):
    name: str
    identity_card: str
    phone: str
    credit_card: str
    debt: float

    class Config:
        orm_mode = True


class ShowSale(BaseModel):
    id_client: int
    amount: int
    sale_date: datetime

    class Config:
        orm_mode = True


class ShowUser(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True



