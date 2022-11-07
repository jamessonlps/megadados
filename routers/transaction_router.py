from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from docs.Tags import Tags

from sqlalchemy.orm import Session
from db.crud import crud_transaction, crud_inventory
from db.provider import get_db
from db.schemas import transaction as SchemaTransaction


router = APIRouter(
    prefix="/transaction",
    tags=[Tags.transactions],
)


@router.get(
    path="/",
    response_model=list[SchemaTransaction.Transaction],
    summary="Get all transactions in database"
)
def get_transactions(db: Session = Depends(get_db)):
    transactions = crud_transaction.get_transactions(db=db)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(transactions)
    )


@router.post(
    path="/{product_id}/",
    response_model=SchemaTransaction.Transaction,
    summary="Create a new transaction to a product (increase or decrease)"
)
def set_transaction(product_id: int, quantity: int, db: Session = Depends(get_db)):
    if quantity == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Quantity must non-zero"
        )
    product_amount = crud_inventory.get_inventory_by_product(db=db, product_id=product_id)
    # All products are created with inventory. If its inventory does not exists,
    # the product was not created or it was deleted.
    if product_amount is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )

    return crud_transaction.create_transaction(db=db, product_id=product_id, quantity=quantity)