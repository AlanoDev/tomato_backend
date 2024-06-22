import abc
from tomato.repository.model import ArticleModel
from tomato.domain import Article
import datetime


class IArticleDao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_articles(self) -> list[Article]:
        pass

    @abc.abstractmethod
    def get_by_id(self, id: int) -> Article | None:
        pass

    @abc.abstractmethod
    def get_by_title(self, title: str) -> Article | None:
        pass

    @abc.abstractmethod
    def create(self, article: Article) -> int:
        pass

    @abc.abstractmethod
    def update(self, article: Article) -> int:
        pass

    @abc.abstractmethod
    def get_by_disease(self, disease: int) -> list[Article]:
        pass

    @abc.abstractmethod
    def delete(self, id: int) -> int:
        pass


class ArticleDao(IArticleDao):# dao对peewee基本api

    def get_articles(self) -> list[Article]:
        return list(ArticleModel.select())

    def get_by_id(self, id: int) -> Article | None:
        return ArticleModel.get_or_none(id=id)

    def get_by_title(self, title: str) -> Article | None:
        return ArticleModel.get_or_none(title=title)

    def get_by_disease(self, disease: int) -> list[Article]:
        return list(ArticleModel.select().where(ArticleModel.disease == disease))

    def create(self, article: Article) -> int:
        try:
            ret = ArticleModel.create(title=article.title, content=article.content, image=article.image,
                                      created_date=datetime.datetime.now(), disease=article.disease)
            return ret.id
        except Exception as e:
            print(e)
            return -1

    def update(self, article: Article) -> int:
        car = self.get_by_id(article.id)
        if car is not None:
            car.title = article.title if len(
                article.title) != 0 else car.title
            car.content = article.content if len(
                article.content) != 0 else car.content
            car.image = article.image if len(article.image) != 0 else car.image
            car.updated_date = datetime.datetime.now()
            car.disease = article.disease
            car.save()
            return 0
        return -1

    def delete(self, id: int) -> int:
        try:
            ArticleModel.delete_by_id(id)
            return 0
        except:
            return -1
