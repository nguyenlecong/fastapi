# Create a simple API

from typing import Optional, List, Set

from fastapi import FastAPI, Query, Path, Body  # import class FastAPI() từ thư viện fastapi
from pydantic import BaseModel, Field  # import class BaseModel của thư viện pydantic


app = FastAPI()  # gọi constructor và gán vào biến app


@app.get("/")  # giống flask, khai báo phương thức get và url
async def root():  # do dùng ASGI nên ở đây thêm async, nếu bên thứ 3 không hỗ trợ thì bỏ async đi
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int = Path(..., title="The ID of the item to get", ge=1),\
                    q: Optional[List[str]] = Query(None, max_length=250, alias="item-query"),\
                    short: bool = False):
    '''
    param item_id: format int
    param q: format string, default value: None, Optional: help you find error that happen
    param short: với định dạng boolean có giá trị mặc định là False
    '''
    item = {"item_id": item_id}
    if short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    if q:
        item.update({"q": q})
    return item


# Order
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

# Path in Path
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

# key-value
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}] # pair format: key-value
@app.get("/dbitems/")
async def read_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]  # trả về dữ liệu từ skip đến skip + limit

# Multiple path and query parameters
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: str):
    item = {"item_id": item_id, "owner_id": user_id}
    return item

# Pydantic Models
class Image(BaseModel):
    url: str
    name: str

class Item(BaseModel):  # kế thừa từ class Basemodel và khai báo các biến
    name: str
    description: Optional[str] = Field(None, title="The description of the item", max_length=300)
    price: float = Field(..., gt=0, description="The price must be greater than zero")
    tax: Optional[float] = None
    tags: List[str] = []
    ingredient: Set[str] = set()
    image: Optional[Image] = None
    images: Optional[List[Image]] = None


@app.post("/items/")
async def create_item(item: Item):  # khai báo dưới dạng parameter
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

# Request body + path parameters
class User(BaseModel):
    username: str
    full_name: Optional[str] = None

@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, user: User,\
                      importance: int = Body(..., gt=0),\
                      q: Optional[str] = None):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    return results
