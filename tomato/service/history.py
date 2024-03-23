from tomato.repository.history import IHistoryRepository
from tomato.domain import History


class HistoryService():
    def __init__(self, repository: IHistoryRepository):
        self.repository: IHistoryRepository = repository

    def create(self, history: History) -> int:
        return self.repository.create(history)

    def delete(self, id: int):
        self.repository.delete(id)

    def get_by_user(self, user_id: int) -> list[History]:
        return self.repository.get_by_user(user_id)