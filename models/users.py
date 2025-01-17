from sqlalchemy import Column,String,Integer
from config.database import base

class users(base): 
    __tablename__ = 'users'

    id = Column(Integer,primary_key=True)
    nick = Column(String)
    country = Column(String)
    score = Column(Integer)