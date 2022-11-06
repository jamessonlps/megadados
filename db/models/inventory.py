from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from ..database import Base

class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Integer)
    product_id = Column(Integer, ForeignKey("products.id"), unique=True)

    product = relationship("Product")