from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from ..database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(32))
    brand = Column(String(32))
    description = Column(String(256), default=None)
    price = Column(Float)