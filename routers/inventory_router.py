from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from docs.Tags import Tags
from db.crud import crud_inventory
from db.provider import get_db


router = APIRouter(
    prefix="/inventory",
    tags=[Tags.inventory],
)


@router.get(
    path="/"
)
def get_full_inventory(db: Session = Depends(get_db)):
    return crud_inventory.get_inventory(db=db)


@router.get("/{product_id}/")
def get_inventory_by_product(product_id: int, db: Session = Depends(get_db)):
    product_inventory = crud_inventory.get_inventory_by_product(db=db, product_id=product_id)
    if product_inventory is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Inventory not found"
        )
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(product_inventory)
    )
