from fastapi import FastAPI
from pydantic import BaseModel
from scalar_fastapi import get_scalar_api_reference

app = FastAPI()


class User(BaseModel):
    name: str
    age: int | None = None
    email: str


@app.get("/scalar", include_in_schema=False)
async def scalar_html():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar FastAPI Reference",
    )


@app.get("/")
def read_root():
    return {"message": "World"}


@app.get("/about")
def read_about():
    return {"message": "This is the about page."}


@app.post("/products")
def create_products():
    return {"message": "Product created successfully."}


@app.put("/products")
def update_products():
    return {"message": "Product updated successfully."}


@app.delete("/products")
def delete_products():
    return {"message": "Product deleted successfully."}


@app.patch("/products")
def patch_products():
    return {"message": "Product patched successfully."}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"userid": user_id, "message": "User retrieved successfully."}


@app.get("/items/")
def get_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit, "message": "Items retrieved successfully."}


@app.post("/create_user")
def create_user():
    return {"message": "User created successfully."}


@app.post("/create_users/")
def create_users(user: User):
    return {
        "message": "Users created successfully.",
        "name": user.name,
        "age": user.age,
        "email": user.email,
    }
