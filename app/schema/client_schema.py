from pydantic import BaseModel


class ClientSchema(BaseModel):
    id: int
    name: str
    identity_card: str
    phone: str
    credit_card: str
    debt: float

    class Config:
        orm_mode = True

