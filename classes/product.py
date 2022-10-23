from uuid import UUID
from pydantic import BaseModel, Field


class ProductBase(BaseModel):
    name: str = Field(example="Pão brioche")
    brand: str = Field(example="Santa Padaria")
    description: str | None = Field(default=None, example="Pão brioche do tipo bola, para você fazer aquele burger perfeito! Huuuuummmm...")
    price: float = Field(example=12.5, ge=0)
    amount: int = Field(default=0, ge=0, example=0)

class Product(ProductBase):
    id: UUID