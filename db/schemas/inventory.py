from pydantic import BaseModel

class InventoryBase(BaseModel):
    amount: int
    product_id: int


class InventoryCreate(InventoryBase):
    pass


class Inventory(InventoryBase):
    id: int
    class Config:
        orm_mode = True