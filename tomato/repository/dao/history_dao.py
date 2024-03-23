import abc
from tomato.repository.model import HistoryModel
from tomato.domain import History
import datetime


class IHistoryDao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_by_user(self, user_id: int) -> list[History]:
        pass

    @abc.abstractmethod
    def create(self, history: History) -> int:
        pass

    @abc.abstractmethod
    def delete(self, id: int):
        pass


class HistoryDao(IHistoryDao):

    def get_by_user(self, user_id: int) -> list[History]:
        return list(HistoryModel.select().where(HistoryModel.user==user_id))

    def create(self, history: History) -> int:
        return HistoryModel.create(user=history.user,
                            time=int(datetime.datetime.now().timestamp()),
                            image=history.image,
                            disease=history.disease).id

    def delete(self, id: int):
        HistoryModel.delete_by_id(id)
