from sqlalchemy.orm.session import Session
from routers.schemas import UserBase
from data.model import User

def create_user(db : Session, request : UserBase) :
    new_user = User(
        user_name = UserBase.username,
        email = UserBase.email,
        password = UserBase.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
