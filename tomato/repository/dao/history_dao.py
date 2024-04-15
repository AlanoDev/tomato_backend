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
        return list(HistoryModel.select().where(HistoryModel.user == user_id))

    def create(self, history: History) -> int:
<<<<<<< HEAD
        try:
            ret = HistoryModel.create(
                user=history.user_id, article_id=history.article_id, created_date=datetime.datetime.now())
            return ret.id
        except:
            return -1
=======
        return HistoryModel.create(user=history.user_id,
                                   article_id=history.article_id).id
>>>>>>> 958f7de38644deb8adc406be6ace9a815a4adea7

    def delete(self, id: int):
        try:
            HistoryModel.delete_by_id(id)
            return 0
        except:
            return -1
