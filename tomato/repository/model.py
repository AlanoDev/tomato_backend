from peewee import *
from tomato.repository import BaseModel, init_database


class UserModel(BaseModel):   # peewee提供的映射
    name = CharField(unique=True)
    email = CharField()
    password = CharField()
    role = CharField()

    class Meta:
        table_name = "user"


class ArticleModel(BaseModel):
    title = CharField(unique=True)
    content = TextField()
    image = CharField(max_length=3000)
    disease = IntegerField()

    class Meta:
        table_name = "article"


class DiseaseModel(BaseModel):
    title = CharField(unique=True)
    description = TextField()
    prevention = TextField()
    healing = TextField()

    class Meta:
        table_name = "disease"


class HistoryModel(BaseModel):
    id = AutoField()
    user = IntegerField()
    article_id = IntegerField()

    class Meta:
        table_name = "history"
        indexes = (
            (('user', 'article_id'), True),
        )


class FavoriteModel(BaseModel):
    id = AutoField()
    user = IntegerField()
    article_id = IntegerField()

    class Meta:
        table_name = "favorite"
        indexes = (
            (('user', 'article_id'), True),
        )


def database_migrate():
    init_database().create_tables(
        [UserModel, ArticleModel, HistoryModel, DiseaseModel, FavoriteModel])
