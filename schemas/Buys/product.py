from pydantic import BaseModel, Field
from datetime import date
class Product_purchase(BaseModel):
    id:int = Field(ge=0,le=1000)
    name:str = Field(min_length=5, max_length=10)
    price:float = Field(ge=0,le=1000)
    acount:float = Field(ge=0,le=1000)
    total:float = Field(ge=0,le=1000)
    created:date
