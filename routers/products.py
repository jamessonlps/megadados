from uuid import UUID, uuid4
from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from classes.product import Product, ProductBase
from docs.Tags import Tags
from others.products_data import products

class Message(BaseModel):
    detail: str


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
    tags=[Tags.products],
    responses={
        200: {
            "model": Product,
            "description": "Product requested by ID",
        },
        404: {
            "model": Message,
            "description": "Product not found",
        }
    }
)
async def get_product(product_id: UUID):
    """Get one product by `id`"""
    for p in products:
        if p["id"] == product_id:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
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
    tags=[Tags.products],
    responses={
        201: {
            "model": Product,
            "description": "Product successful created."
        }
    }
)
async def create_product(product: ProductBase):
    """Create a new product and return the product created if success."""
    product_dict = product.dict()
    product_dict = { "id": uuid4(), **product_dict}
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
                status_code=status.HTTP_200_OK,
                content={"message": "Product deleted"}
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
            # Localiza e deleta produto da lista
            idx = products.index(p)
            products.pop(idx)
            
            # Cria um objeto produto com os campos antigos
            stored_product_model = Product(**p)
            
            # Inicializa objeto de produto com os dados a serem atualizados
            update_data = product.dict(exclude_unset=True)
            
            # Faz cópia do objeto antigo atualizando os campos a serem alterados
            updated_product = stored_product_model.copy(update=update_data)
            
            # Grava produto atualizado na lista de produtos e retorna o produto atualizado
            product_updated = jsonable_encoder(updated_product)
            product_updated = { "id": product_id, **product_updated }
            products.append(product_updated)
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=product_updated
            )
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Product not found"
    )