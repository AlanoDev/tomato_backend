from tomato.repository.article import IArticleRepository
from tomato.repository.history import IHistoryRepository
from tomato.domain import History
from tomato.repository.user import IUserRepository


class HistoryService():
    def __init__(self, repository: IHistoryRepository, user_repository: IUserRepository, article_repository: IArticleRepository):
        self.repository: IHistoryRepository = repository
        self.user_repository: IUserRepository = user_repository
        self.article_repository: IArticleRepository = article_repository

    def create(self, history: History) -> int:
        if self.user_repository.get_by_id(history.user_id) is None:
            return -1
        if self.article_repository.get_by_id(history.article_id) is None:
            return -1
        return self.repository.create(history)

    def delete(self, id: int) -> int:
        if self.get_by_id(id) is None:
            return -1
        return self.repository.delete(id)

    def get_by_user(self, user_id: int) -> list[History]:
        return self.repository.get_by_user(user_id)
