from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base #Se importa el objeto Base desde el archivo database.py

class News(Base): 

    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50),index=True)
    ulr = Column(String(50),index=True)
    date = Column(String(50),index=True)
    title = Column(String(50),index=True)
    media_outlet = Column(String(50),index=True)
    
    category = relationship("Category", back_populates="owner")
    
class Category(Base):

    __tablename__ = "has_category"
    
    id = Column(Integer, primary_key=True, index=True)	
    my_category = Column(String(50), index=True)
    value = Column(Boolean, default=True)


    owner = relationship("News", back_populates="category")
