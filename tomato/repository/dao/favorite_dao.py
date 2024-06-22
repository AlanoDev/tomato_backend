import abc
import datetime
from tomato.repository.model import FavoriteModel
from tomato.domain import Favorite


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
    def delete(self, id: int) -> int:
        pass


class FavoriteDao(IFavoriteDao):

    def get_favorites(self) -> list[Favorite]:
        return list(FavoriteModel.select())

    def get_by_id(self, id: int) -> Favorite | None:
        return FavoriteModel.get_or_none(id=id)

    def get_by_user(self, user_id: int) -> list[Favorite]:
        ret = []
        for item in list(FavoriteModel.select().where(FavoriteModel.user == user_id)):
            ret.append(Favorite(favorite_id=item.id,
                       user_id=item.user, article_id=item.article_id))

        return ret

    def create(self, favorite: Favorite) -> int:
        try:

            ret = FavoriteModel.create(
                user=favorite.user_id, article_id=favorite.article_id, created_date=datetime.datetime.now())
            return ret.id
        except:
            return -1

    def delete(self, id: int) -> int:
        try:
            FavoriteModel.delete_by_id(id)
            return 0
        except:
            return -1
