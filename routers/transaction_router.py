from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from docs.Tags import Tags

from sqlalchemy.orm import Session
from db.crud import crud_transaction, crud_inventory
from db.provider import get_db


router = APIRouter(
    prefix="/transaction",
    tags=[Tags.transactions],
)


@router.get("/")
def get_transactions(db: Session = Depends(get_db)):
    return crud_transaction.get_transactions(db=db)


@router.post("/{product_id}/")
def set_transaction(product_id: int, quantity: int, db: Session = Depends(get_db)):
    product_amount = crud_inventory.get_inventory_by_product(db=db, product_id=product_id)

    if product_amount is None:
        crud_inventory.create_inventory(db=db, product_id=product_id, amount=0) # CORRIGIR DEPOIS PARA CASOS PARTICULARES

    return crud_transaction.create_transaction(db=db, product_id=product_id, quantity=quantity)