from typing import List, Optional

from pydantic import BaseModel


class CategoryBase(BaseModel):
    my_category: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    value: bool

    class Config:
        orm_mode = True

class NewsBase(BaseModel):
    title: str
    url: str
    date = str
    title = str
    media_outlet = str

class NewsCreate(NewsBase):
    pass


class News(NewsBase):
    id: int
    category: List[Category] = []
    
    class Config:
        orm_mode = True

