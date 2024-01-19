from fastapi import FastAPI
from data.database import engine
from routers import users,posts
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(users.router)
app.include_router(posts.router)
app.mount("/images", StaticFiles(directory='images'), name = 'images')


