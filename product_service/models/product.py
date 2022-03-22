from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, DateTime
from product_service.database import Base
from sqlalchemy.orm import relationship


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)

    brand = Column(String, index=True)
    model = Column(String, index=True)
    price = Column(Integer)
    production_time = Column(DateTime)

    admin_id = Column(Integer)
