from sqlalchemy import Column,Boolean,Integer,ForeignKey,String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base=declarative_base()
#declarative basemodel 
class User(Base):
    __tablename__ = 'users_table'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    hobby = Column(String(100), nullable=False)


#creating the  pydantic basemodel

class UserBase(BaseModel):
    id:int
    user_id: int
    name:str
    age:int
    hobby:str

    