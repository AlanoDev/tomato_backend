from fastapi import APIRouter
from tomato.repository.dao.article_dao import ArticleDao
from tomato.repository.article import ArticleRepository
from tomato.service.article import ArticleService
from tomato.repository.dao.user_dao import UserDao
from tomato.repository.user import UserRepository
from tomato.domain import Article as ArticleDomain
from pydantic import BaseModel

router = APIRouter(prefix='/article')

ad = ArticleDao()
ud = UserDao()
ur = UserRepository(ud)
ar = ArticleRepository(ad)
asv = ArticleService(ar,ur)

class Article(BaseModel):
    tittle: str
    content: str
    image: str|None

@router.get('/all')
async def get_all_articles():
    return asv.get_all_articles()


@router.get('/{user_id}')
async def get_by_user(user_id: int):
    return asv.get_by_user(user_id)


@router.get('/')
async def get_by_tittle(tittle: str):
    return asv.get_by_tittle(tittle)

@router.post('/')
async def create(article: Article,user_id:int):
    domain=ArticleDomain(tittle=article.tittle, content=article.content, image=article.image,user=user_id)
    return asv.create(domain)

@router.put('/')
async def update(article: Article):
    domain=ArticleDomain(id=article.id, tittle=article.tittle, content=article.content, image=article.image)
    return asv.update(domain)

@router.delete('/')
async def delete(id: int):
    return asv.delete(id)
