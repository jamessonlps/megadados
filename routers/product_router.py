from uuid import UUID, uuid4
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from classes.product import Product, ProductBase
from docs.Tags import Tags

from db.crud import crud_product
from db.provider import get_db
from db.schemas import product as SchemaProduct

class Message(BaseModel):
    detail: str



router = APIRouter(
    prefix="/products",
    tags=[Tags.products],
)



@router.get("/", response_model=list[Product], summary="Get a list of products")
def get_products(db: Session = Depends(get_db)):
    """Return a list of all products stored in database."""
    all_products = crud_product.get_products(db)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(all_products),
    )

@router.get("/{product_id}/")
def get_product(product_id: int, db: Session = Depends(get_db)):
    return crud_product.get_product_by_id(db=db, product_id=product_id)


@router.post("/")
def create_product(product: SchemaProduct.ProductCreate, db: Session = Depends(get_db)):
    return crud_product.create_product(db=db, product=product)


# ==============================================================



# @router.get(
#     "/{product_id}/", 
#     response_model=Product,
#     summary="Get a single product by id",
#     tags=[Tags.products],
#     responses={
#         200: {
#             "model": Product,
#             "description": "Product requested by ID",
#         },
#         404: {
#             "model": Message,
#             "description": "Product not found",
#         }
#     }
# )
# async def get_product(product_id: UUID):
#     """Get one product by `id`"""
#     for p in products:
#         if p["id"] == product_id:
#             return JSONResponse(
#                 status_code=status.HTTP_200_OK,
#                 content=jsonable_encoder(p)
#             )
#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND, 
#         detail="Product not found"
#     )


# @router.post(
#     "/", 
#     response_model=Product,
#     summary="Create a new product",
#     tags=[Tags.products],
#     responses={
#         201: {
#             "model": Product,
#             "description": "Product successful created."
#         }
#     }
# )
# async def create_product(product: ProductBase):
#     """Create a new product and return the product created if success."""
#     product_dict = product.dict()
#     product_dict["id"] = uuid4()
#     products.append(product_dict)
#     return JSONResponse(
#         status_code=status.HTTP_201_CREATED,
#         content=jsonable_encoder(product_dict)
#     )


# @router.delete(
#     "/{product_id}/",
#     summary="Delete a single product",
#     tags=[Tags.products]
# )
# async def delete_product(product_id: UUID):
#     for p in products:
#         if p["id"] == product_id:
#             products.remove(p)
#             return JSONResponse(
#                 status_code=status.HTTP_200_OK,
#                 content={"message": "Product deleted"}
#             )
#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND, 
#         detail="Product not found"
#     )


# @router.put(
#     "/{product_id}/",
#     summary="Update a single product",
#     response_model=Product,
#     tags=[Tags.products]
# )
# async def update_product(product_id: UUID, product: ProductBase):
#     for p in products:
#         if p["id"] == product_id:
#             idx = products.index(p)
#             products.pop(idx)
#             stored_product_model = Product(**p)
#             update_data = product.dict(exclude_unset=True)
#             updated_product = stored_product_model.copy(update=update_data)
#             p = jsonable_encoder(updated_product)
#             products.append(p)
#             return JSONResponse(
#                 status_code=status.HTTP_200_OK,
#                 content=p
#             )
#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND, 
#         detail="Product not found"
#     )