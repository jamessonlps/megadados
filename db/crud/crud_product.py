from sqlalchemy.orm import Session

from ..models import product as ModelProduct
from ..schemas import product as SchemaProduct


def get_products(db: Session):
    return db.query(ModelProduct.Product).all()


def get_product_by_id(db: Session, product_id: int):
    return db.query(ModelProduct.Product).filter(ModelProduct.Product.id == product_id).first()


def create_product(db: Session, product: SchemaProduct.ProductCreate):
    db_product = ModelProduct.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product