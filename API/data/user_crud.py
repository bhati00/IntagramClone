from more_itertools import first
from sqlalchemy.orm.session import Session
from routers.schemas import UserBase
from data.model import User
from .hashing import Hash
from fastapi import HTTPException, status
from more_itertools import first

def create_user(db : Session, request : UserBase) :
    new_user = User(
        user_name = request.user_name,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_by_username(db : Session, username : str):
    user = db.query(User).filter(User.user_name == username).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail= 'user with {username} not found')
    return user


    
