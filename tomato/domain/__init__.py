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
    tittle: str | None = None
    content: str | None = None
    image: str | None = None
    user: int = 0


class Disease(BaseModel):
    title: str | None = None
    introduction: str | None = None
    prevention: str | None = None
    healing: str | None = None


class History(BaseModel):
    history_id: int = 0
    user_id: int = 0
    image: str | None = None
    disease_id: int = 0
