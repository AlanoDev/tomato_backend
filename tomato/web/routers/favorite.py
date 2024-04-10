from fastapi import APIRouter
from tomato.domain import Favorite
from tomato.repository.favorite import FavoriteRepository
from tomato.repository.dao.favorite_dao import FavoriteDao
from tomato.service.favorite import FavoriteService
router = APIRouter(prefix='/favorite')

fd = FavoriteDao()
fr = FavoriteRepository(fd)
fs = FavoriteService(fr)

@router.get('/')
async def get_all_favorite(user_id: int):
    return fs.get_by_user(user_id)

@router.delete('/')
async def delete_favorite(id: int):
    return fs.delete(id)

@router.post('/')
async def create_favorite(user_id: int, article_id: int):
    domain = Favorite(user_id=user_id, article_id=article_id)
    return fs.create(domain)