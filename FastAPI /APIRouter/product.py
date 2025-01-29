#from main import AddProduct
from model import AddProduct
from fastapi import APIRouter

router = APIRouter()

@router.get("/get_products/")
async def get_product(get_products: AddProduct):
          return get_products

@router.post("/add_product/")
async def add_product(create_product: AddProduct):
          add_products = AddProduct(name = create_product.name, price=create_product.price)
          return add_products