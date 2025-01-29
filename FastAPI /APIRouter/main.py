from fastapi import FastAPI
from pydantic import BaseModel
from product import router

app = FastAPI()

@app.get('/')
def read_root(): 
    return {"Hello": "World"}

app.include_router(router=router)
# class AddProduct(BaseModel):
#     name: str
#     price: float





