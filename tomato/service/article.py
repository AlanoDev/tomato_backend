from tomato.repository.article import IArticleRepository
from tomato.repository.disease import IDiseaseRepository
from tomato.repository.user import IUserRepository
from tomato.domain import Article


class ArticleService():
    def __init__(self, article_repository: IArticleRepository, user_repository: IUserRepository, disease_repository: IDiseaseRepository):
        self.article = article_repository
        self.user = user_repository
        self.disease = disease_repository

    def create(self, article: Article) -> int:
        if self.disease.get_by_id(article.disease) is None:
            return -1
        return self.article.create(article)

    def delete(self, id: int) -> int:
        if self.get_by_id(id) is None:
            return -1
        return self.article.delete(id)

    def get_by_id(self, id: int) -> Article | None:
        return self.article.get_by_id(id)

    def update(self, article: Article) -> int:
        if self.disease.get_by_id(article.disease) is None:
            return -1
        return self.article.update(article)

    def get_all_articles(self):
        return self.article.get_articles()

    def get_by_disease(self, disease: int) -> list[Article]:
        return self.article.get_by_disease(disease)

    def get_by_title(self, title: str) -> Article | None:
        return self.article.get_by_title(title)
