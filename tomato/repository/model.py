from peewee import *;
from tomato.repository import BaseModel,init_database

class UserModel(BaseModel):
    name=CharField(unique=True)
    email=CharField()
    password=CharField()
    role=CharField()
    class Meta:
        table_name="user"

class ArticleModel(BaseModel):
    tittle=CharField(unique=True)
    content=TextField()
    image=CharField(max_length=3000)
    disease=IntegerField()
    class Meta:
        table_name="article"

class DiseaseModel(BaseModel):
    tittle=CharField(unique=True)
    description=TextField()
    prevention=TextField()
    healing=TextField()
    class Meta:
        table_name="disease"

class HistoryModel(BaseModel):
    user=IntegerField()
    article_id=IntegerField()
    class Meta:
        table_name="history"

class FavoriteModel(BaseModel):
    user=IntegerField()
    article_id=IntegerField()
    class Meta:
        table_name="favorite" 


def database_migrate():
    init_database().create_tables([UserModel,ArticleModel,HistoryModel,DiseaseModel,FavoriteModel])