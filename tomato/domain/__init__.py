import datetime

from pydantic import BaseModel


class User(BaseModel):
    id: int = 0
    name: str | None = None
    email: str | None = None
    password: str | None = None
    role: str | None = None


class Article(BaseModel):
    id: int = 0
    title: str | None = None
    content: str | None = None
    image: str | None = None
    disease: int = 0


class Disease(BaseModel):
    id: int = 0
    title: str | None = None
    description: str | None = None
    prevention: str | None = None
    healing: str | None = None


class History(BaseModel):
    history_id: int = 0
    user_id: int = 0
    article_id: int = 0
    time: str | None = None


class Favorite(BaseModel):
    favorite_id: int = 0
    user_id: int = 0
    article_id: int = 0
