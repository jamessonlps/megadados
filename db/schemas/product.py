from pydantic import BaseModel, Field


class ProductBase(BaseModel):
    name: str = Field(example="Pão brioche")
    brand: str = Field(example="Santa Padaria")
    description: str | None = Field(default=None, example="Pão brioche do tipo bola, para você fazer aquele burger perfeito! Huuuuummmm...")
    price: float = Field(example=12.5, ge=0)


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True