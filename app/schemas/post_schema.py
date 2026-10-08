from datetime import datetime

from pydantic import BaseModel, ConfigDict


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    ratings: int | None = None


class PostResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    content: str
    published: bool
    ratings: int
    created_at: datetime