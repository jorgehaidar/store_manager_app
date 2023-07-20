from pydantic import BaseModel
from datetime import datetime


class SaleSchema(BaseModel):
    id: int
    id_item: int
    id_client: int
    amount: int
    sale_date: datetime

    class Config:
        orm_mode = True
        