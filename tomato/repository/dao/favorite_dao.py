import abc
from tomato.repository.model import FavoriteModel
from tomato.domain import Favorite
import datetime


class IFavoriteDao(metaclass=abc.ABCMeta):
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
    def delete(self, id: int):
        pass


class FavoriteDao(IFavoriteDao):

    def get_favorites(self) -> list[Favorite]:
        return list(FavoriteModel.select())

    def get_by_id(self, id: int) -> Favorite | None:
        return FavoriteModel.get_or_none(id=id)

    def get_by_user(self, user_id: int) -> list[Favorite]:
        return list(FavoriteModel.select().where(FavoriteModel.user == user_id))

    def create(self, favorite: Favorite) -> int:
        return FavoriteModel.create(user=favorite.user_id, article_id=favorite.article_id).id

    def delete(self, id: int):
        FavoriteModel.get_by_id(id).delete_instance()
