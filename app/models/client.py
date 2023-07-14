from pydantic import BaseModel


class Client(BaseModel):
    id: int
    name: str
    identity_card: int
    phone: str
    credit_card: int
    debt: int
