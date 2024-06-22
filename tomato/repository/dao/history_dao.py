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
        ret = []
        for item in list(HistoryModel.select().where(HistoryModel.user == user_id)):
            ret.append(History(history_id=item.id, user_id=item.user,
                       article_id=item.article_id))
        return ret

    def create(self, history: History) -> int:
        try:
            ret = HistoryModel.create(
                user=history.user_id, article_id=history.article_id, created_date=datetime.datetime.now())
            return ret.id
        except:
            return -1

    def delete(self, id: int):
        try:
            HistoryModel.delete_by_id(id)
            return 0
        except:
            return -1
