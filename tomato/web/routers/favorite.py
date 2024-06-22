from fastapi import APIRouter
from pydantic import BaseModel
from tomato.domain import Favorite
from tomato.repository.article import ArticleRepository
from tomato.repository.dao.article_dao import ArticleDao
from tomato.repository.dao.user_dao import UserDao
from tomato.repository.favorite import FavoriteRepository
from tomato.repository.dao.favorite_dao import FavoriteDao
from tomato.repository.user import UserRepository
from tomato.service.favorite import FavoriteService
from tomato.web.utils.results import handle_results
router = APIRouter(prefix='/favorite')

fd = FavoriteDao()
fr = FavoriteRepository(fd)
ud = UserDao()
ur = UserRepository(ud)
ad = ArticleDao()
ar = ArticleRepository(ad)
fs = FavoriteService(fr, ur, ar)


class Favorite(BaseModel):
    id: int | None=None
    user_id: int
    article_id: int


@router.get('/{id}')
async def get_all_favorite(id: int):
    res = fs.get_by_user(id)
    res_list: list[Favorite] = []
    for item in res:
        res_list.append(
            Favorite(id=item.favorite_id, user_id=item.user_id, article_id=item.article_id))
    return handle_results(False, 'Success', res_list, 0)


@router.delete('/{id}')
async def delete_favorite(id: int):
    if fs.delete(id) == -1:
        return handle_results(True, '', None, 20+2)
    return handle_results(False, 'Success', None, 0)


@router.post('/')
async def create_favorite(user_id: int, article_id: int):
    domain = Favorite(user_id=user_id, article_id=article_id)
    if fs.create(domain) == -1:
        return handle_results(True, '', None, 20+1)
    return handle_results(False, 'Success', None, 0)
