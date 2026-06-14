from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from scalar_fastapi import get_scalar_api_reference
from typing import Optional, List

app = FastAPI()

fake_db = [
    {"id": 1, "mouse": "Logitech MX Master 3", "price": 99.99},
    {"id": 2, "mouse": "Razer DeathAdder V2", "price": 69.99},
    {"id": 3, "mouse": "Apple Magic Mouse 2", "price": 79.99},
]


class Product(BaseModel):
    id: int
    mouse: str
    price: float


class ProductUpdate(BaseModel):
    mouse: Optional[str] = None
    price: Optional[float] = None


@app.get("/scalar", include_in_schema=False)
async def scalar_html():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar FastAPI Reference",
    )


@app.get("/")
def read_root():
    return {"message": "World"}


@app.get("/products", response_model=List[Product])
def get_products():
    return fake_db


@app.get("/products{product_id}", response_model=Product)
def get_products(product_id: int):
    return fake_db
    for product in fake_db:
        if product["id"] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")


@app.post("/products", response_model=Product, status_code=201)
def create_products(product: Product):
    for p in fake_db:
        if p["id"] == product.id:
            raise HTTPException(
                status_code=400, detail="Product with this ID already exists"
            )
    fake_db.append(product.dict())
    return product


@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, product: Product):
    for index, product in enumerate(fake_db):
        if p["id"] == product_id:
            stored_item_model = Product(**p)
            update_data = product.dict(exclude_unset=True)
            updated_item = stored_item_model.copy(update=update_data)

            fake_db[index] = updated_item.model_dump()
            return updated_item
    raise HTTPException(status_code=404, detail="Product not found")


app.delete("/products/{product_id}", status_code=204)


def delete_product(product_id: int):
    for index, product in enumerate(fake_db):
        if product["id"] == product_id:
            fake_db.pop(index)
            return {"message": "Product deleted successfully."}
        HTTPException(status_code=404, detail="Product not found")
