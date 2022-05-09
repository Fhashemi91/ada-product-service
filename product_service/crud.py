from hashlib import sha1
from sqlalchemy.orm import Session

from product_service.models.product import Product
from product_service import schemas


def get_or_create(db: Session, model, **kwargs):
    instance = db.query(model).filter_by(**kwargs).first()
    if not instance:
        instance = model(**kwargs)
        db.add(instance)
        db.commit()

    return instance


def get_product(db: Session, product_id: int):
    return db.query(Product).filter_by(id=product_id).first()


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Product).offset(skip).limit(limit).all()


def add_product(db: Session, info: schemas.ProductCreate, admin_id):
    product = db.query(Product).filter_by(brand=info.brand, model=info.model).first()
    if not product:
        product = Product(brand=info.brand, model=info.model, amount=0, admin_id=admin_id)

    if info.price:
        product.price = info.price

    product.amount += 1
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def update_product_amount(db: Session, product_id: int, admin_id: id, amount: int):
    product = db.query(Product).filter_by(id=product_id).first()
    if not product:
        return

    product.amount = amount
    db.add(product)
    db.commit()

    db.refresh(product)
    return product


def update_product_price(db: Session, product_id: int, admin_id: id, price: int):
    product = db.query(Product).filter_by(id=product_id).first()
    if not product:
        return

    product.price = price
    db.add(product)
    db.commit()

    db.refresh(product)
    return product
