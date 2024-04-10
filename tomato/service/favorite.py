from tomato.domain import Favorite
from tomato.repository.favorite import IFavoriteRepository


class FavoriteService():
    def __init__(self, repository: IFavoriteRepository):
        self.repository = repository

    def get_favorites(self) -> list[Favorite]:
        return self.repository.get_favorites()

    def get_by_user(self, user_id: int) -> list[Favorite]:
        return self.repository.get_by_user(user_id)

    def get_by_id(self, id: int) -> Favorite | None:
        return self.repository.get_by_id(id)

    def create(self, favorite: Favorite) -> int:
        return self.repository.create(favorite)

    def delete(self, id: int):
        self.repository.delete(id)
