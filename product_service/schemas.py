from datetime import datetime
from pydantic import BaseModel


class ProductBase(BaseModel):
    id: int
    brand: str
    model: str
    price: int
    production_time: datetime


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    brand: str
    model: str
    price: int
    production_time: datetime

    class Config:
        orm_mode = True
