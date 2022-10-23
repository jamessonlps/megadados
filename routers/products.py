from uuid import UUID, uuid4
from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from classes.product import Product, ProductBase
from docs.Tags import Tags
from others.products_data import products


router = APIRouter(
    prefix="/products",
    tags=[Tags.products],
)


@router.get(
    "/", 
    response_model=list[Product],
    summary="Get a list of products",
    tags=[Tags.products]
)
async def get_products():
    """Return a list of all products stored in database."""
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(products),
    )


@router.get(
    "/{product_id}/", 
    response_model=Product,
    summary="Get a single product by id",
    tags=[Tags.products]
)
async def get_product(product_id: UUID):
    """Get one product by `id`"""
    for p in products:
        if p["id"] == product_id:
            return JSONResponse(
                status=status.HTTP_200_OK,
                content=jsonable_encoder(p)
            )
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Product not found"
    )


@router.post(
    "/", 
    response_model=Product,
    summary="Create a new product",
    tags=[Tags.products]
)
async def create_product(product: ProductBase):
    """Create a new product and return the product created if success."""
    product_dict = product.dict()
    product_dict["id"] = uuid4()
    products.append(product_dict)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=jsonable_encoder(product_dict)
    )


@router.delete(
    "/{product_id}/",
    summary="Delete a single product",
    tags=[Tags.products]
)
async def delete_product(product_id: UUID):
    for p in products:
        if p["id"] == product_id:
            products.remove(p)
            return JSONResponse(
                status_code=status.HTTP_204_NO_CONTENT
            )
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Product not found"
    )


@router.put(
    "/{product_id}/",
    summary="Update a single product",
    response_model=Product,
    tags=[Tags.products]
)
async def update_product(product_id: UUID, product: ProductBase):
    for p in products:
        if p["id"] == product_id:
            idx = products.index(p)
            products.pop(idx)
            stored_product_model = Product(**p)
            update_data = product.dict(exclude_unset=True)
            updated_product = stored_product_model.copy(update=update_data)
            p = jsonable_encoder(updated_product)
            products.append(p)
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=p
            )
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Product not found"
    )