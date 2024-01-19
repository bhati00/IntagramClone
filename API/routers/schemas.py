from pydantic import BaseModel
from datetime import datetime

# users pydantic model
class UserBase(BaseModel):
    user_name : str
    email : str
    password: str

class UserDisplay(BaseModel):
    user_name : str
    email : str
    class Config():
        orm_mode = True

class User(BaseModel):
    user_name: str
    class Config():
        orm_mode = True


# posts pyndantic model
class PostBase(BaseModel):
    image_url : str
    image_url_type : str
    caption : str
    user_id : int

class PostDisplay(BaseModel):
    id : int
    image_url : str
    image_url_type : str
    caption : str
    timestamp : datetime
    user : User
    class Config():
        orm_mode = True
        arbitrary_types_allowed = True



          

        
