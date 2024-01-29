from fastapi import FastAPI
from data.database import engine
from routers import users,posts
from fastapi.staticfiles import StaticFiles
from auth import authentication
from auth import googleAuth

app = FastAPI()
app.include_router(users.router)
app.include_router(posts.router)
app.include_router(authentication.router)
app.include_router(googleAuth.router)
app.mount("/images", StaticFiles(directory='images'), name = 'images')


