from fastapi import FastAPI
from routers import products

description = """
James Bond API's helps you do awesome stuff. 🚀

## Products

You will be able to:

* **Read a single product**.
* **Read a list of products**.
* **Create product**.
* **Edit a product**.
* **Delete a product**.
"""

app = FastAPI(
    title="James Bond API",
    description=description,
    version="1.0.1",
    contact={
        "name": "Jamesson Leandro Paiva Santos",
        "email": "jamessonlps@al.insper.edu.br",
    },
)

app.include_router(products.router)