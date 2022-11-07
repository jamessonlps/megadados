from pydantic import BaseModel, Field

class TransactionBase(BaseModel):
    quantity: int = Field(example=1)
    product_id: int = Field(example=1)


class TransactionCreate(TransactionBase):
    pass


class Transaction(TransactionBase):
    id: int
    class Config:
        orm_mode = True