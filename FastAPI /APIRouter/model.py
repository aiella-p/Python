from pydantic import BaseModel


class AddProduct(BaseModel):
    name: str
    price: float