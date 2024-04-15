from tomato.repository.dao.article_dao import IArticleDao
from tomato.domain import Article
import abc


class IArticleRepository(metaclass=abc.ABCMeta):
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


class ArticleRepository(IArticleRepository):
    def __init__(self, dao: IArticleDao):
        self.dao: IArticleDao = dao

    def get_articles(self) -> list[Article]:
        return self.dao.get_articles()

    def get_by_id(self, id: int) -> Article | None:
        return self.dao.get_by_id(id)

    def get_by_title(self, title: str) -> Article | None:
        return self.dao.get_by_title(title)

    def create(self, article: Article) -> int:
        return self.dao.create(article)

    def update(self, article: Article) -> int:
        return self.dao.update(article)

    def get_by_disease(self, disease: int) -> list[Article]:
        return self.dao.get_by_disease(disease)

    def delete(self, id: int) -> int:
        return self.dao.delete(id)
