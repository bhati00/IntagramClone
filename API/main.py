from fastapi import FastAPI
from data import model
from data.database import engine
from routers import users

app = FastAPI()
app.include_router(users.router)

# generating our tables
model.Base.metadata.create_all(engine)

@app.get("/root")
def root():
    return "Hello world"
