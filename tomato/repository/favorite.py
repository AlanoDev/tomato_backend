import abc
import datetime
from tomato.domain import Favorite
from tomato.repository.dao.favorite_dao import IFavoriteDao

<<<<<<< HEAD

=======
>>>>>>> 958f7de38644deb8adc406be6ace9a815a4adea7
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
<<<<<<< HEAD
    def delete(self, id: int) -> int:
        pass


=======
    def delete(self, id: int):
        pass

>>>>>>> 958f7de38644deb8adc406be6ace9a815a4adea7
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

<<<<<<< HEAD
    def delete(self, id: int)->int:
        return self.dao.delete(id)
=======
    def delete(self, id: int):
        self.dao.delete(id)
>>>>>>> 958f7de38644deb8adc406be6ace9a815a4adea7
