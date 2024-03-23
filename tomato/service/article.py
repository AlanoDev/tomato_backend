from tomato.repository.article import IArticleRepository
from tomato.repository.user import IUserRepository
from tomato.domain import Article



class ArticleService():
    def __init__(self, article_repository: IArticleRepository, user_repository: IUserRepository):
        self.article = article_repository
        self.user = user_repository

    def create(self,article: Article) -> int:
        if self.user.get_by_id(article.user) is None:
            return -2
        if self.article.get_by_tittle(article.tittle) is not None:
            return -1
        return self.article.create(article)

    def delete(self, id: int) -> int:
        if self.article.get_by_id(id) is not None:
            self.article.delete(id)
            return 0
        return -1

    def update(self, article: Article) -> int:
        if self.article.get_by_id(article.id) is not None:
            self.article.update(article)
            return 0
        return -1

    def get_all_articles(self):
        return self.article.get_articles()

    def get_by_user(self, user_id: int) -> list[Article]:
        return self.article.get_by_user(user_id)

    def get_by_tittle(self, tittle: str) -> Article | None:
        return self.article.get_by_tittle(tittle)
