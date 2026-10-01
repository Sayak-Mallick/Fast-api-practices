from random import randrange

import psycopg2
import time
from fastapi import FastAPI, HTTPException, Response, status
from psycopg2._psycopg import cursor
from psycopg2.extras import RealDictCursor
from pydantic import BaseModel

app = FastAPI()  # creating an instance of FastAPI


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    ratings: int | None = None

while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='872320022', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("✅ Database connected successfully")
        break
    except Exception as error:
        print("❌ Connection to database failed")
        print("Error: ", error)
        time.sleep(2)

# Routes (Path Operations) - make path operation function as descriptive as possible
@app.get("/")  # this decorator actually helps to define the route and HTTP method
def health():
    return {"message": "Welcome to my API"}


@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts""")
    posts = cursor.fetchall()
    return {"data": posts}


# @app.post("/createposts")
# def create_posts(payload: dict = Body(...)):
#     print(payload)
#     return {"new_post": f"{payload['title']} created"}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    cursor.execute("""INSERT INTO posts (title, content, published, ratings) VALUES (%s, %s, %s, %s) RETURNING *  """,(post.title, post.content, post.published, post.ratings))
    new_post = cursor.fetchone()
    conn.commit() # we need to commit after every insertion
    return {"data": new_post}  # return the post as a response


@app.get("/posts/latest")
def get_latest_post():
    # the latest entry into the database
    cursor.execute("""SELECT * FROM posts ORDER BY id DESC LIMIT 1""")
    post = cursor.fetchone()
    return {"data": post}


@app.get("/posts/{id}")  # This is not the best way to get the single data
def get_single_post(id: int):
    cursor.execute("""SELECT * FROM posts WHERE id = %s""", (id,))
    post = cursor.fetchone()
    if not post:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": "Post not found"}
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} cannot be found"
        )
    return {"data": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id),))
    post = cursor.fetchone()
    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {id} does not exist",
        )
    conn.commit() # Commit the changes to the database
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    cursor.execute(
        """UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""",
        (post.title, post.content, post.published, str(id))
    )
    post = cursor.fetchone()
    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {id} cannot be found",
        )
    conn.commit()     # Commit changes to the database
    return {"data": post}
