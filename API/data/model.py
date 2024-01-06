from .database import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key = True, index = True)
    user_name = Column(String)
    email = Column(String)
    password = Column(String)