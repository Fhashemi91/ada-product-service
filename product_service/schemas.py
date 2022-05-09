from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class ProductBase(BaseModel):
    id: int
    brand: str
    model: str
    price: Optional[int]

class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    brand: str
    model: str
    price: Optional[int]
    amount: int

    class Config:
        orm_mode = True
