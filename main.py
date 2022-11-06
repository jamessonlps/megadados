from fastapi import FastAPI
from routers import inventory_router, product_router, transaction_router

from db.database import engine
from db.models import product, inventory

product.Base.metadata.create_all(bind=engine)
inventory.Base.metadata.create_all(bind=engine)

description = """
James Bond API's helps you do awesome stuff. 🚀

## Products

* **Read a single product**.
* **Read a list of products**.
* **Create product**.
* **Edit a product**.
* **Delete a product**.

## Inventory

* **Read inventory data**
* **Read a product inventory**
"""

app = FastAPI(
    title="James Bond API",
    description=description,
    version="1.0.0",
    contact={
        "name": "Jamesson Leandro Paiva Santos",
        "email": "jamessonlps@al.insper.edu.br",
    },
)

app.include_router(product_router.router)
app.include_router(inventory_router.router)
app.include_router(transaction_router.router)