from tomato.domain import Favorite
from tomato.repository.article import IArticleRepository
from tomato.repository.favorite import IFavoriteRepository
from tomato.repository.user import IUserRepository


class FavoriteService():
    def __init__(self, repository: IFavoriteRepository, user_repository: IUserRepository, article_repository: IArticleRepository):
        self.repository = repository
        self.user_repository: IUserRepository = user_repository
        self.article_repository: IArticleRepository = article_repository

    def get_favorites(self) -> list[Favorite]:
        return self.repository.get_favorites()

    def get_by_user(self, user_id: int) -> list[Favorite]:
        return self.repository.get_by_user(user_id)

    def get_by_id(self, id: int) -> Favorite | None:
        return self.repository.get_by_id(id)

    def create(self, favorite: Favorite) -> int:
        print(favorite)
        if self.user_repository.get_by_id(favorite.user_id) is None:
            return -1
        if self.article_repository.get_by_id(favorite.article_id) is None:
            return -1
        return self.repository.create(favorite)

    def delete(self, id: int) -> int:
        if self.get_by_id(id) is None:
            return -1
        return self.repository.delete(id)
