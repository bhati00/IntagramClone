from sqlalchemy.orm.session import Session
from routers.schemas import UserBase
from data.model import User
from .hashing import Hash

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
