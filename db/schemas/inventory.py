from pydantic import Field
from pydantic import BaseModel

class InventoryBase(BaseModel):
    amount: int = Field(default=0, ge=0, example=0)
    product_id: int = Field(example=1)


class InventoryCreate(InventoryBase):
    pass


class Inventory(InventoryBase):
    id: int
    class Config:
        orm_mode = True