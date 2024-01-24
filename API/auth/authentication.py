from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import  OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from data.model import User
from data import database, hashing
from auth import oauth2

router = APIRouter(tags= ['authentication'])

@router.post('/login')
def login(request : OAuth2PasswordRequestForm = Depends(), db :Session = Depends(database.get_db)):
    user = db.query(User).filter(request.username == User.user_name).first()
    if not user:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail = "user {request.username} not found"
        )
    if not hashing.Hash.verify_passowrd(user.password, request.password):
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail = "user {request.username} not found"
        )
    access_token = oauth2.create_access_token(data = {"username": user.user_name})
    return {
        'access_token' : access_token,
        'token_type' : 'bearer',
        'user_id' : user.id,
        'username' : user.user_name
    }

    