import abc
import datetime
from tomato.domain import Favorite
from tomato.repository.dao.favorite_dao import IFavoriteDao

class IFavoriteRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_favorites(self) -> list[Favorite]:
        pass

    @abc.abstractmethod
    def get_by_user(self, user_id: int) -> list[Favorite]:
        pass

    @abc.abstractmethod
    def get_by_id(self, id: int) -> Favorite | None:
        pass

    @abc.abstractmethod
    def create(self, favorite: Favorite) -> int:
        pass

    @abc.abstractmethod
    def delete(self, id: int) -> int:
        pass


class FavoriteRepository():

    def __init__(self, dao: IFavoriteDao):
        self.dao: IFavoriteDao = dao

    def get_favorites(self) -> list[Favorite]:
        return self.dao.get_favorites()

    def get_by_user(self, user_id: int) -> list[Favorite]:
        return self.dao.get_by_user(user_id)

    def get_by_id(self, id: int) -> Favorite | None:
        return self.dao.get_by_id(id)

    def create(self, favorite: Favorite) -> int:
        return self.dao.create(favorite)

    def delete(self, id: int)->int:
        return self.dao.delete(id)
