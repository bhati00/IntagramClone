from fastapi import APIRouter, Depends
from routers.schemas import UserBase
from sqlalchemy.orm.session import Session
from data.database import get_db
from data.user_crud import create_user

router = APIRouter(
    prefix= '/user',
    tags= ['user']
)

@router.post('', response_model= UserBase)
def create_user(request = UserBase, db : Session = Depends(get_db())):
    return create_user(UserBase, Session)
