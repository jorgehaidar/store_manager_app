from datetime import datetime
from pydantic import BaseModel


class Sales(BaseModel):
    id: int
    id_item: int
    id_client: int
    amount: int
    sale_date: datetime
