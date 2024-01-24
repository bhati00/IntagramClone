from locale import currency
from fastapi import APIRouter, Depends, status, UploadFile, File
from fastapi.exceptions import HTTPException
from routers.schemas import PostDisplay, PostBase, UserAuth
from sqlalchemy.orm.session import Session
from data.database import get_db
from data import post_crud
from typing import List
import random
import string
import shutil
from auth import oauth2

router = APIRouter(
    prefix= '/post',
    tags= ['post']
)
image_url_types = ['absolute','relative']

# create post
@router.post('', response_model= PostDisplay)
def create_post(request : PostBase, db : Session = Depends(get_db), current_user : UserAuth = Depends(oauth2.get_current_user)):
    if not request.image_url_type in image_url_types:
        raise HTTPException(status_code= status.HTTP_422_UNPROCESSABLE_ENTITY,
                             detail="Please Proivde a URL Type")
    return post_crud.create_post(db, request)

# return all posts 
@router.get('/all', response_model= List[PostDisplay])
def posts(db : Session = Depends(get_db), current_user : UserAuth = Depends(oauth2.get_current_user)):
    return post_crud.get_posts(db)

# upload an image 
@router.post('/image')
def upload_image(image : UploadFile = File(...), current_user : UserAuth = Depends(oauth2.get_current_user)):
    letter = string.ascii_letters
    rand_string = ''.join(random.choice(letter) for i in range(6))
    new = f'_{rand_string}.'
    filename = new.join(image.filename.rsplit('.',1))
    path = f'images/{filename}' 

    with open(path, "w+b") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {'filename' :path}
