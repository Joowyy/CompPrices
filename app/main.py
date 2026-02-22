from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database.db import engine, get_db
from app.database import models
from app.services.price_service import PriceService
from app.schemas import ProductCreate, ProductResponse

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

service = PriceService()


@app.post("/products", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return service.create_product(db, product.name, product.url)


@app.get("/products", response_model=list[ProductResponse])
def list_products(db: Session = Depends(get_db)):
    return service.list_products(db)