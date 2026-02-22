from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    url: str

class ProductResponse(BaseModel):
    id: int
    name: str
    url: str

    class Config:
        from_attributes = True