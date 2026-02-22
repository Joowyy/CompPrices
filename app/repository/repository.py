from sqlalchemy.orm import Session
from app.database.models import Product


class ProductRepository:

    def create(self, db: Session, name: str, url: str) -> Product:
        product = Product(name=name, url=url)
        db.add(product)
        db.commit()
        db.refresh(product)
        return product

    def get_all(self, db: Session):
        return db.query(Product).all()