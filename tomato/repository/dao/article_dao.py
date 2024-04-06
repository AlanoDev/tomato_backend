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
    def get_by_tittle(self, tittle: str) -> Article | None:
        pass

    @abc.abstractmethod
    def create(self, article: Article) -> int:
        pass

    @abc.abstractmethod
    def update(self, article: Article):
        pass

    @abc.abstractmethod
    def delete(self, id: int):
        pass


class ArticleDao(IArticleDao):

    def get_articles(self) -> list[Article]:
        return list(ArticleModel.select())

    def get_by_id(self, id: int) -> Article | None:
        return ArticleModel.get_or_none(id=id)

    def get_by_tittle(self, tittle: str) -> Article | None:
        return ArticleModel.get_or_none(tittle=tittle)

    def create(self, article: Article) -> int:
        return ArticleModel.create(tittle=article.tittle, content=article.content, image=article.image, create_datetime=datetime.datetime.now(), disease=article.disease).id

    def update(self, article: Article):
        car: ArticleModel = ArticleModel.get_by_id(article.id)
        car.tittle = article.tittle if len(article.tittle) != 0 else car.tittle
        car.content = article.content if len(
            article.content) != 0 else car.content
        car.image = article.image if len(article.image) != 0 else car.image
        car.updated_date = datetime.datetime.now()
        car.disease = article.disease if len(
            article.disease) != 0 else car.disease
        car.save()

    def delete(self, id: int):
        ArticleModel.delete_by_id(id)
