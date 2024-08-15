from pydantic import BaseModel
from datetime import date


class Product_purchase(BaseModel):
    id:int
    name:str
    price:float
    acount:float
    total:float
    created:date
