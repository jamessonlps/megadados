from sqlalchemy.orm import Session


from ..models import transaction as ModelTransaction
from db.crud.crud_inventory import update_inventory


def get_transactions(db: Session) -> list[ModelTransaction.Transaction]:
    return db.query(ModelTransaction.Transaction).all()


def create_transaction(db: Session, product_id: int, quantity: int):
    update_inventory(db=db, product_id=product_id, quantity=quantity)

    db_transaction = ModelTransaction.Transaction(product_id=product_id, quantity=quantity)
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction