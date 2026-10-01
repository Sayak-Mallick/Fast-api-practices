from random import randrange

from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel

app = FastAPI()  # creating an instance of FastAPI


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    ratings: int | None = None


my_posts = [
    {"id": 1, "title": "Title of Post 1", "content": "Content of Post 1"},
    {"id": 2, "title": "Title of Post 2", "content": "Content of Post 2"},
]


# Routes (Path Operations) - make path operation function as descriptive as possible
@app.get("/")  # this decorator actually helps to define the route and HTTP method
def root():
    return {"message": "Welcome to my API"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


# @app.post("/createposts")
# def create_posts(payload: dict = Body(...)):
#     print(payload)
#     return {"new_post": f"{payload['title']} created"}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(new_post: Post):
    post_dict = new_post.dict()  # convert the Pydantic model to a dictionary
    post_dict["id"] = randrange(0, 1000000)  # generate a random ID for the post
    my_posts.append(post_dict)  # add the post to the list of posts
    return {"new_post": post_dict}  # return the post as a response


def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p
    return None


@app.get("/posts/latest")
def get_latest_post():
    post = my_posts[len(my_posts) - 1]
    return {"data": post}


@app.get("/posts/{id}")  # This is not the best way to get the single data
def get_single_post(id: int):
    post = find_post(id)
    if not post:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": "Post not found"}
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )
    return {"data": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {id} cannot be found",
        )
    my_posts.remove(post)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int, updated_post: Post):
    post = find_post(id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} cannot be found",
        )
    post.update(updated_post.dict())
    return {"data": post}
