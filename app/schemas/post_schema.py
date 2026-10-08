from datetime import datetime

from pydantic import BaseModel


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    ratings: int | None = None


class PostResponse(BaseModel):
    id: str
    title: str
    content: str
    pubished: bool
    ratings: int | None = None
    created_at: datetime
