from .database import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

# user table
class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key = True, index = True)
    user_name = Column(String)
    email = Column(String)
    password = Column(String)
    items = relationship('Post', back_populates = 'user')

# post table
class Post(Base):
    __tablename__ = 'Posts'
    id = Column(Integer, primary_key = True, index = True)
    image_url = Column(String)
    image_url_type = Column(String)
    caption = Column(String)
    timestamp = Column(DateTime)
    user_id = Column(Integer, ForeignKey(User.id))
    user = relationship('User', back_populates = ('items'))




