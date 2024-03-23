from tomato.repository.dao.history_dao import IHistoryDao
from tomato.domain import History
import abc
class IHistoryRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create(self, history: History) -> int:
        pass

    @abc.abstractmethod
    def delete(self, id: int):
        pass

    @abc.abstractmethod
    def get_by_user(self, user_id: int) -> list[History]:
        pass

class HistoryRepository():
    def __init__(self, dao: IHistoryDao):
        self.dao: IHistoryDao = dao

    def create(self, history: History) -> int:
        return self.dao.create(history)

    def delete(self, id: int):
        self.dao.delete(id)

    def get_by_user(self, user_id: int) -> list[History]:
        return self.dao.get_by_user(user_id)
