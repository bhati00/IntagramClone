from sqlalchemy.orm.session import Session
from datetime import datetime
from routers.schemas import PostBase
from data.model import Post

# creating post 
def create_post(db : Session, request : PostBase):
    new_post =  Post(
        image_url = request.image_url,
        image_url_type = request.image_url_type,
        caption = request.caption,
        timestamp = datetime.utcnow(),     
        user_id = request.user_id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_posts(db : Session):
    return db.query(Post).all()
    
