from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    brand: str
    description: str | None = None
    price: float


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True