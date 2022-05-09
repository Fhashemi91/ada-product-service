from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, DateTime, UniqueConstraint
from product_service.database import Base
from sqlalchemy.orm import relationship


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)

    brand = Column(String)
    model = Column(String)
    price = Column(Integer)
    amount = Column(Integer, default=1)

    admin_id = Column(Integer)

    __table_args = UniqueConstraint('brand', 'model', name='_unique_model_name')
