from sqlalchemy.orm import Session

from ..models import inventory as ModelInventory


def get_inventory(db: Session) -> list[ModelInventory.Inventory]:
    return db.query(ModelInventory.Inventory).all()


def get_inventory_by_product(db: Session, product_id: int) -> ModelInventory.Inventory | None:
    return db.query(ModelInventory.Inventory).filter(ModelInventory.Inventory.id == product_id).first()


def create_inventory(db: Session, product_id: int, amount: int) -> ModelInventory.Inventory:
    db_product_inventory = ModelInventory.Inventory(
        product_id=product_id, 
        amount=amount
    )
    db.add(db_product_inventory)
    db.commit()
    db.refresh(db_product_inventory)
    return db_product_inventory


def update_inventory(db: Session, product_id: int, quantity: int) -> ModelInventory.Inventory:
    db_inventory = get_inventory_by_product(db=db, product_id=product_id)
    db_inventory.amount += quantity
    try:
        db.commit()
        db.refresh(db_inventory)
        return db_inventory
    except:
        db.rollback()
        raise Exception