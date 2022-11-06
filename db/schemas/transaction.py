from pydantic import BaseModel

class TransactionBase(BaseModel):
    quantity: int
    product_id: int


class TransactionCreate(TransactionBase):
    pass


class Transaction(TransactionBase):
    id: int
    class Config:
        orm_mode = True