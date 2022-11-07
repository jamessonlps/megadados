from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from ..models import product as ModelProduct, inventory as ModelInventory
from ..schemas import product as SchemaProduct

from .crud_inventory import create_inventory


def get_products(db: Session):
    return db.query(ModelProduct.Product).all()


def get_product_by_id(db: Session, product_id: int) -> ModelProduct.Product:
    product = db.query(ModelProduct.Product).filter(ModelProduct.Product.id == product_id).first()
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return product


def create_product(db: Session, product: SchemaProduct.ProductCreate) -> ModelProduct.Product:
    # Create a new product
    db_product = ModelProduct.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    product_created = product.dict()
    product_created["id"] = db_product.id
    # Create a inventory to the new product with initial amount equals 0
    create_inventory(db=db, product_id=db_product.id, amount=0)
    
    return product_created


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