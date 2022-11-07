from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from docs.Tags import Tags

from db.crud import crud_product
from db.provider import get_db
from db.schemas import product as SchemaProduct


router = APIRouter(
    prefix="/products",
    tags=[Tags.products],
)


@router.get(
    path="/", 
    response_model=list[SchemaProduct.Product], 
    summary="Get a list of products"
)
def get_products(db: Session = Depends(get_db)):
    """
        Return a list of all products stored in database.
    """
    all_products = crud_product.get_products(db)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(all_products),
    )


@router.get(
    path="/{product_id}/",
    response_model=SchemaProduct.Product,
    summary="Get a product by id"
)
def get_product(product_id: int, db: Session = Depends(get_db)):
    """
        Return a single product by its `id` if exists.
    """
    db_product = crud_product.get_product_by_id(db=db, product_id=product_id)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(db_product)
    )


@router.post(
    path="/", 
    response_model=SchemaProduct.Product, 
    summary="Create a new product"
)
def create_product(product: SchemaProduct.ProductCreate, db: Session = Depends(get_db)):
    """
        Create and register a new product in database. It also create a inventory to product with amount equals 0.
    """
    product = crud_product.create_product(db=db, product=product)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=jsonable_encoder(product)
    )


@router.put(
    path="/{product_id}/",
    response_model=SchemaProduct.Product,
    summary="Update a single product"
)
def update_product(product_id: int, product: SchemaProduct.ProductBase, db: Session = Depends(get_db)):
    """
        Update current data from a product.
    """
    product = crud_product.update(db=db, product_id=product_id, product=product)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(product)
    )


@router.delete(
    path="/{product_id}/",
    summary="Delete a single product"
)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    """
        Delete a product: by doing this, 
        all inventory and transactions from this product will be deleted too.
    """
    crud_product.delete(db=db, product_id=product_id)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={ "message": "Product deleted" }
    )