from fastapi import FastAPI
from app.database.db import engine
from app.database import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "API En funcionamiento! :D"}