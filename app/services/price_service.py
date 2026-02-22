from sqlalchemy.orm import Session
from app.repository.repository import ProductRepository


class PriceService:

    def __init__(self):
        self.repository = ProductRepository()

    def create_product(self, db: Session, name: str, url: str):
        if not name:
            raise ValueError("Product name cannot be empty")

        if not url.startswith("http"):
            raise ValueError("Invalid URL")

        return self.repository.create(db, name, url)

    def list_products(self, db: Session):
        return self.repository.get_all(db)