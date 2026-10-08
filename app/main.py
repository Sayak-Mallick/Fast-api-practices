from fastapi import Depends, FastAPI, HTTPException, Response, status
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from . import models
from .database import engine, get_db
from .schemas.post_schema import Post, PostResponse
from .schemas.users_schema import User, UserResponse

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
models.Base.metadata.create_all(
    bind=engine
)  # this will create the tables in the database if they do not exist

app = FastAPI()  # creating an instance of FastAPI


# Routes (Path Operations) - make path operation function as descriptive as possible
@app.get("/")  # this decorator actually helps to define the route and HTTP method
def health():
    return {"message": "Welcome to my API"}


@app.get("/posts")
def get_posts(db: Session = Depends(get_db), response_model=PostResponse):
    posts = db.query(models.Post).all()
    return posts


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(
    post: Post,
    db: Session = Depends(get_db),
    response_model=PostResponse,
):
    new_post = models.Post(
        **post.dict()
    )  # this will unpack the post object into a dictionary and pass it to the Post model
    db.add(new_post)  # this will add the new_post object to the database session
    db.commit()  # we need to commit after every insertion
    db.refresh(
        new_post
    )  # this will refresh the new_post object with the data from the database,
    return {"data": new_post}  # return the post as a response


@app.get("/posts/latest")
def get_latest_post(db: Session = Depends(get_db)):
    post = (
        db.query(models.Post).order_by(models.Post.id.desc()).first()
    )  # this will get the latest post from the database
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"No posts found"
        )
    return {"data": post}


@app.get("/posts/{id}")  # This is not the best way to get the single data
def get_single_post(
    id: int, db: Session = Depends(get_db), response_model=PostResponse
):
    post = (
        db.query(models.Post).filter(models.Post.id == id).first()
    )  # this will get the post with the given id from the database
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} cannot be found",
        )
    return {"data": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    post = (
        db.query(models.Post)
        .filter(models.Post.id == id)
        .delete(synchronize_session=False)
    )  # this will delete the post with the given id from the database
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} cannot be found",
        )
    db.commit()  # Commit the changes to the database
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(
    id: int,
    updated_post: Post,
    db: Session = Depends(get_db),
    response_model=PostResponse,
):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {id} was not found",
        )

    post_query.update(updated_post.model_dump(), synchronize_session=False)
    db.commit()
    return {"data": post_query.first()}


@app.get("/users")
def get_users(db: Session = Depends(get_db), response_model=UserResponse):
    users = db.query(models.User).all()
    return {"data": users}


@app.post("/users", status_code=status.HTTP_201_CREATED, response_model=User)
def create_user(user: User, db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"data": new_user}
