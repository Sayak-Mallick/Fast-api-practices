from fastapi import FastAPI
from passlib.context import CryptContext

from .database import Base, engine
from .models.posts_model import Post
from .models.users_model import User
from .routes.post_routes import router as post_router
from .routes.user_routes import router as user_router

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# this will create the tables in the database if they do not exist
Base.metadata.create_all(bind=engine)

app = FastAPI()  # creating an instance of FastAPI


app.include_router(post_router)
app.include_router(user_router)


# Routes (Path Operations) - make path operation function as descriptive as possible
@app.get("/")  # this decorator actually helps to define the route and HTTP method
def health():
    return {"message": "Welcome to my API"}
