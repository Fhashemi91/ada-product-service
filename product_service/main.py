from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from product_service import crud, schemas
from product_service.models.product import Product
from product_service.database import engine, Base, SessionLocal

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def verify_admin() -> bool:
    # TODO This method integrates with the user management system to verify if a
    # user has admin access to manage inventory or not.
    return True


@app.post("/products/new/{admin_id}", response_model=schemas.Product)
def register_product(
    admin_id: str, info: schemas.ProductCreate, db: Session = Depends(get_db)
):
    return crud.add_product(db=db, info=info, admin_id=admin_id)


@app.get("/products", response_model=list[schemas.Product])
def list_product(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = crud.get_products(db, skip=skip, limit=limit)
    return products


@app.get("/products/{product_id}", response_model=schemas.Product)
def list_product(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_id)
    return product


@app.post("/products/update/amount/{admin_id}", response_model=schemas.Product)
def update_amount(
        admin_id: str, product_id: int, amount: int, db: Session = Depends(get_db)
):
    return crud.update_product_amount(db, product_id, admin_id, amount)


@app.post("/products/update/price/{admin_id}", response_model=schemas.Product)
def update_amount(
        admin_id: str, product_id: int, price: int, db: Session = Depends(get_db)
):
    return crud.update_product_price(db, product_id, admin_id, price)
