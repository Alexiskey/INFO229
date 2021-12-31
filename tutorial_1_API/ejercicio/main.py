from typing import List
from typing import Optional

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#/v1/news?f=2021-01-01&to=2021-01-31&category=sport
@app.get("/v1/{news}")
async def read_news(
    news:str, f: str = "2021-01-01" , to:str = "2021-01-31", category:str= 'sport' 
):

    item = {"id": int, "title": "string", "url":"string", "date":"string", "media_outlet":"string", "category":"string"}
    
    return item
