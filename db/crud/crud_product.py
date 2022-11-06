from sqlalchemy.orm import Session

from ..models import product as ModelProduct
from ..schemas import product as SchemaProduct


def get_products(db: Session):
    return db.query(ModelProduct.Product).all()


def get_product_by_id(db: Session, product_id: int) -> ModelProduct.Product:
    return db.query(ModelProduct.Product).filter(ModelProduct.Product.id == product_id).first()


def create_product(db: Session, product: SchemaProduct.ProductCreate) -> ModelProduct.Product:
    db_product = ModelProduct.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def update(db: Session, product_id: int, product: SchemaProduct.ProductBase) -> ModelProduct.Product:
    db_product = get_product_by_id(db=db, product_id=product_id)
    
    db_product.name = product.name
    db_product.brand = product.brand
    db_product.price = product.price
    db_product.description = product.description

    db.commit()
    db.refresh(db_product)

    return db_product


def delete(db: Session, product_id: int) -> None:
    db_product = get_product_by_id(db=db, product_id=product_id)
    db.delete(db_product)
    db.commit()
    return None