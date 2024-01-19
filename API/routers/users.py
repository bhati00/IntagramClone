from fastapi import APIRouter, Depends
from routers.schemas import UserBase, UserDisplay
from sqlalchemy.orm.session import Session
from data.database import get_db
from data import user_crud

router = APIRouter(
    prefix= '/sign-in',
    tags= ['user']
)

@router.post('', response_model= UserDisplay)
def create_user(request : UserBase, db : Session = Depends(get_db)):
    return user_crud.create_user(db, request)
